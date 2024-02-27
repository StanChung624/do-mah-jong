from Deck import Deck
from CheckUtility import *
from typing import Dict
from abc import ABC, abstractmethod

class Player():
    def __init__(self, holding:list=None, is_owner:int=-1, index:int=0, deck:Deck=None) -> None:
        
        self.deck = deck

        self.__set_initial_condition()
        # load holding
        if holding:
            self.holding = holding
            for card in holding:
                self.tracker[card]-=1
        else:
            self.holding = list()

        # owner of the game
        self.owner = is_owner

        # playing sequence
        self.index = index

    def __set_initial_condition(self):
        # card tracker by player
        self.tracker = dict()

        for card in Deck.unique_card:
            self.tracker[card] = 4
        
        for i in range(4):
            self.tracker['x'+str(i+1)] = 4
            self.tracker['X'+str(i+1)] = 4

        #holding
        self.holding = list()
        # flower
        self.flower = list()

        # saw card temporary storage
        self.saw_card = ""
        self.eat_combinations = []
        self.can_eat = False
        self.can_pon = False
        self.can_gan = False
        self.can_win = False

    def reset(self) -> None:
        self.__set_initial_condition()        

    def _sort(action):
        def wrapper(self, *args, **kwargs):            
            self.holding.sort()
            return action(self, *args, **kwargs)
        return wrapper
    
    def _action_decorator(action):
        def wrapper(self, *args, **kwargs):
            announce = kwargs.setdefault("announce", False)
            if announce:
                print(action.__name__)
            action(self, *args, **kwargs)
            self.__reset_action()                    
        return wrapper
    
    @abstractmethod
    def ditch(self)->str:
        return None


    @_action_decorator
    def pon(self, **kwargs):
        self.flower += [self.saw_card]*3
        for i in range(2):
            self.holding.remove(self.saw_card)
    
    @_action_decorator
    def gan(self, **kwargs):
        self.flower += [self.saw_card]*4
        for i in range(3):
            self.holding.remove(self.saw_card)
        print("amend :", self.draw_card())
        self.amend_flower()

    @_action_decorator
    def eat(self, **kwargs):
        kwargs.setdefault("formation", None)        
        if kwargs["formation"] is None:
            for i in range(len(self.eat_combinations)):
                print(i+1, ":", self.eat_combinations[i])
            kwargs["formation"] = self.eat_combinations[int(input(":"))-1]
        self.flower += kwargs["formation"]
        self.holding.remove(kwargs["formation"][0])
        self.holding.remove(kwargs["formation"][-1])

    def __reset_action(self)->None:
        self.can_eat = False
        self.can_pon = False
        self.can_gan = False
        self.can_win = False
    
    def is_owner(self)->int:
        return self.owner    
    
    def set_is_owner(self, owner_index:int)->None:
        self.owner = owner_index

    @_sort
    def draw_card(self, *args, **kwargs):
        deck = kwargs.setdefault("deck", self.deck)
        card = kwargs.setdefault("card", None)
        announce = kwargs.setdefault("announce", False)
        if card:
            self.holding.append(card)
            self.tracker[card] -= 1
            self.saw_card = card
            if announce:
                print("draw", card)
            return card
        elif deck:
            card = deck.serve()
            if card:
                self.holding.append(card)            
                self.tracker[card] -= 1
                self.saw_card = card
                if announce:
                    print("draw", card)
                return card
            else:
                return None

    @_sort
    def suggest_ditch(self)->Tuple[Dict[str,int], str]:        
        
        possible_ditch = self.analyze_ditch_to_listen()[1]
        if len(possible_ditch) > 0:
            # print("use analysis result")
            # get best option from analysis            
            most_waits = 0
            ditch_card = ""
            for card, waits in possible_ditch.items():                
                if waits >= most_waits:
                    ditch_card = card
                    most_waits = waits
            return None, ditch_card

        ret = dict()
        for card in self.holding:
            ret[card] = -1

        # for duplicated cards
        for card in self.holding:
            ret[card]+=20

        # for numeric cards in sequence
        for card in self.holding:
            neighbor_cards = get_neighbor(card)
            if neighbor_cards:
                for nei in neighbor_cards:
                    if nei in ret.keys():
                        ret[card] += 1
                        ret[nei] += 1

        # recommend discard card
        discard_card = ""
        lowest_score = 100
        for k, v in ret.items():
            if lowest_score >= v:
                discard_card = k
                lowest_score = v

        return ret, discard_card

    @_sort
    def amend_flower(self, *args, **kwargs):
        deck = kwargs.setdefault("deck", self.deck)
        if not deck:
            print("[err] No card amended, for deck is not specified.")
        
        for card in self.holding:            
            if 'x' in card or 'X' in card:
                self.holding.pop(self.holding.index(card))
                self.flower.append(card)
                self.draw_card(deck)

    @_sort
    def is_win(self):
        return is_win(self.holding)
    
    @_sort
    def show(self, announce:bool=True):
        content = "player index = " + str(self.index) + ", holding:\n"
        content += str(self.flower) + "\n"
        content += str(self.holding) + "\n"
        if announce:
            print(content)
        return content

    def discard_card(self, card:str=None, index:int=None):        
        if card:        
            self.holding.remove(card)
            return card
        elif index:
            index -= 1
            card = self.holding[index]
            self.holding.remove(card)
            return card
        else:
            print("[error] discard card failed.")
            return None
    
    @_sort
    def see(self, card:str, player=None, player_index:int=None)->List[List[str]]:

        self.__reset_action()
        self.saw_card = card
        self.tracker[card] -= 1

        # return in-take combination
        ret = []

        is_upstream_player = True

        if player:
            player_index = player.index
        if player_index is not None:
            is_upstream_player = (self.index + 3) % 4 == player_index
        
        if card in self.holding:
            card_sum = dict()
            for c in self.holding:
                card_sum[c] = 0
            for c in self.holding:
                card_sum[c] += 1

            if card_sum[card] >= 2:
                self.can_pon = True
                # ret.append([card] * 3)
            if card_sum[card] == 3:
                self.can_gan = True
                # ret.append([card] * 4)
        
        
        if card in Deck().l_list or card in Deck().m_list or card in Deck().o_list:
            neighbor_card = get_neighbor(card)            
            self.holding.append(card)
            for i in range(len(neighbor_card)-2):
                if neighbor_card[i] in self.holding and \
                neighbor_card[i+1] in self.holding and \
                neighbor_card[i+2] in self.holding:
                    combination = neighbor_card[i:i+3]
                    combination.remove(card)
                    ret.append([combination[0], card, combination[1]])
                    self.can_eat = is_upstream_player
            
            self.holding.remove(card)            

        if card in self.listen():
            self.can_win = True

        self.eat_combinations = ret

    @_sort
    def listen(self):
        if self.is_win():
            return None
        ret = list()
        for card in Deck.unique_card:
            self.holding.append(card)
            if(self.is_win()):
                ret.append(card)
            self.holding.remove(card)
        return ret
    
    @abstractmethod
    def action(self, **kwargs)->bool:
        return None

    @_sort
    def analyze_ditch_to_listen(self)->Dict[str,List[Dict[str,int]]]:        
        if self.is_win():
            return 
        else:
            ret = dict()
            efficiency = dict()

            tmp_holding = list(self.holding)            
            for card in tmp_holding:               
                self.holding.remove(card)
                listen_cards = self.listen()
                if listen_cards is None:
                    self.show()
                    self.saw_card
                    
                if len(listen_cards) > 0:
                    ret_ = list()
                    waits = 0
                    for lis in listen_cards:
                        ret_.append({lis:self.tracker[lis]})
                        waits += self.tracker[lis]
                    ret[card] = ret_
                    efficiency[card] = waits

                self.holding.append(card)

            return ret, efficiency
