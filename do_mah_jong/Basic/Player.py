from do_mah_jong.Basic.Deck import Deck
from do_mah_jong.Basic.CheckUtility import *
from typing import Dict
from abc import ABC, abstractmethod

class Player():
    def __init__(self,
                 holding:List[str]=None, 
                 is_owner:int=-1,
                 index:int=0, 
                 deck:Deck=None, 
                 seen_cards:Dict[int, List[str]]=None) -> None:
        
        self.deck = deck

        # playing sequence
        self.index = index

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
        self.see_card = ""
        self.seen_cards = self.__set_seen_cards()
        
        self.eat_combinations = []
        self.can_eat = False
        self.can_pon = False
        self.can_gan = False
        self.can_win = False
        self.__is_win = None

        self.last_draw = ""

    def __set_seen_cards(self)->Dict[int, Dict[str,int]]:
        ret = dict()
        other_players = [0,1,2,3]
        other_players.remove(self.index)
        
        counter_dict = dict()
        for card in Deck.unique_card:
            counter_dict[card] = 0

        for i in other_players:
            ret.setdefault(i, dict(counter_dict))
        return ret

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
        self.flower += [self.see_card]*3
        for i in range(2):
            self.holding.remove(self.see_card)
    
    @_action_decorator
    def gan(self, **kwargs):
        if self.holding.count(self.see_card) == 3:
            self.flower += [self.see_card]*4
            while self.holding.count(self.see_card) > 0:
                self.holding.remove(self.see_card)    
            self.draw_card(deck=self.deck)
            self.amend_flower()
        elif self.holding.count(self.see_card) == 4:
            self.flower += [self.see_card]*4
            while self.holding.count(self.see_card) > 0:
                self.holding.remove(self.see_card)
             
            
        
    @_action_decorator
    def self_gan(self, **kwargs):
        # hidden gan
        if self.holding.count(self.see_card) > 1:
            self.flower += [self.see_card]*4
            while self.holding.count(self.see_card) > 0:
                self.holding.remove(self.see_card)
            self.draw_card(deck=self.deck)
            self.amend_flower()
        # out gan
        else:
            gan_card = self.see_card
            id = self.flower.index(gan_card)
            if len(self.flower) > id + 3:
                self.flower = self.flower[0:id] +\
                    [gan_card]*4 + self.flower[id+3:]
            else:
                self.flower = self.flower[0:id] +\
                    [gan_card]*4 
            
            self.draw_card(deck=self.deck)
            self.holding.remove(gan_card)
            self.amend_flower()

    @_action_decorator
    def win(self, **kwargs):
        self.holding.append(self.see_card)
        self.__is_win = True

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
        self.__is_win = None
    
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
            self.see_card = card
            if announce:
                print("draw", card)
            self.last_draw = card
            return card
        elif deck:
            card = deck.serve()
            if card:
                self.holding.append(card)
                self.tracker[card] -= 1
                self.see_card = card
                if announce:
                    print("draw", card)
                self.last_draw = card
                return card
            else:
                return None

    def amend_flower(self, *args, **kwargs):
        deck = kwargs.setdefault("deck", self.deck)
        if not deck:
            print("[err] No card amended, for deck is not specified.")

        f_card = ""
        for card in self.holding:            
            if 'x' in card or 'X' in card:
                f_card = card
                break

        if f_card == "":
            return 
        else:
            self.flower.append(f_card)
            self.holding.remove(f_card)
            self._sort()
            self.draw_card(deck=deck)
            return self.amend_flower()
        
    def is_win(self, ignore_pair:bool=False):
        if self.__is_win is None:
            self.__is_win = is_win(self.holding)
        return self.__is_win
    
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
    def evaluate_action(self, card:str, player=None, player_index:int=None)->List[List[str]]:
        self.__reset_action()
        
        is_upstream_player = True
        if player:
            player_index = player.index
        if player_index is not None:
            is_upstream_player = (self.index + 3) % 4 == player_index

        # return in-take combination
        ret = []
        
        # can pon or gan
        card_sum = dict()
        for c in self.holding:
            card_sum[c] = 0
        for c in self.holding:
            card_sum[c] += 1

        if card in self.holding:
            if card_sum[card] >= 2:
                self.can_pon = True
                # ret.append([card] * 3)
            if card_sum[card] == 3:
                self.can_gan = True
                # ret.append([card] * 4)
        
        if card in self.listen():
            self.can_win = True
            
        # can self gan
        if player_index == self.index:
            # check for flower3 draw 1 gan scenario
            if self.see_card in self.flower:
                in_flw_id = self.flower.index(self.see_card)
                if len(self.flower) > in_flw_id + 2:
                    if self.flower[in_flw_id + 2] == self.see_card and\
                        self.flower[in_flw_id + 1] == self.see_card:
                        self.can_gan = True

            # check for flower3 holding 1 gan scenario
            for c in self.holding:
                if c not in self.flower:
                    continue
                index = self.flower.index(c)
                if self.flower.count(c) == 3:
                    if len(self.flower) >= index + 2:
                        if self.flower[index] == self.flower[index+1] and \
                            self.flower[index] == self.flower[index+2]:
                            self.see_card = c
                            self.can_gan = True
                            return

            # check for holding 4 scenario
            for c, cnt in card_sum.items():
                if cnt == 4:
                    self.see_card = c
                    self.can_gan = True
                    return
        
        if is_upstream_player:
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
                        self.can_eat = True
                
                self.holding.remove(card)            

        self.eat_combinations = ret
        self.holding.sort()
        return ret

    def see(self, card:str=None, player=None, player_index:int=None, card_list:List[str]=None)->List[List[str]]:

        # for see other flower cards case
        if card_list is not None and card is None:
            for card in [card_list[0], card_list[2]]:
                self.tracker[card] -= 1
            return None

        # for see sigle card and react case
        self.see_card = card
        # track other's player played card
        if player_index is not None and player_index != self.index:
            self.seen_cards[player_index][card] += 1
        # track cards in deck
        self.tracker[card] -= 1

        return self.evaluate_action(card, player=player, player_index=player_index)
        

    @_sort
    def listen(self):
        return listen(self.holding)
    
    def is_listen(self):
        if self.__is_win:
            return True
        return len(self.listen()) > 0
    
    @abstractmethod
    def action(self, **kwargs)->bool:
        return None

    
