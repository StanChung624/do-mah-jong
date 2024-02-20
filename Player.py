from Deck import Deck
from CheckUtility import *
from typing import Dict


class Player():
    def __init__(self, holding:list=None, is_owner:int=-1, index:int=0, deck:Deck=None) -> None:
        
        self.deck = deck

        # card tracker by player
        self.tracker = dict()

        for card in Deck.unique_card:
            self.tracker[card] = 4
        
        for i in range(4):
            self.tracker['x'+str(i+1)] = 4
            self.tracker['X'+str(i+1)] = 4

        # flower
        self.flower = list()
        if holding:
            self.holding = holding
            for card in holding:
                self.tracker[card]-=1
        else:
            self.holding = list()

        # owner of the game
        self.is_owner = is_owner

        # playing sequence
        self.index = index

        # saw card temporary storage
        self.saw_card = ""
        self.can_eat = False
        self.can_pon = False
        self.can_gan = False
        self.can_win = False

    def _sort(action):
        def warpper(self, *args, **kwargs):            
            self.holding.sort()
            action(self, *args, **kwargs)
        return warpper
    
    def _action_decorator(action):
        def wrapper(self, card):
            action(self, card)
            self.show()     
            self.__reset_action()       
        return wrapper

    @_action_decorator
    def pon(self, card):
        self.flower += [card]*3
        for i in range(2):
            self.holding.remove(card)
    
    @_action_decorator
    def gan(self, card):
        self.flower += [card]*4
        for i in range(3):
            self.holding.remove(card)

    def __reset_action(self)->None:
        self.can_eat = False
        self.can_pon = False
        self.can_gan = False
        self.can_win = False
    
    def is_owner(self)->int:
        return self.is_owner
    
    @_sort
    def set_is_owner(self, *args, **kwargs)->None:        
        self.is_owner = int(args[0])

    @_sort
    def draw_card(self, *args, **kwargs):
        deck = kwargs.setdefault("deck", self.deck)
        card = kwargs.setdefault("card", None)
        if deck:
            card = deck.serve()
            self.holding.append(card)            
            self.tracker[card] -= 1
            return card
        elif card:
            self.holding.append(card)
            self.tracker[card] -= 1
            return card

    def grade(self)->Tuple[Dict[str,int], str]:
        self.holding.sort()
        if self.is_win():
            return  None, None
        
        possible_ditch = self.analyze()
        if len(possible_ditch) > 0:
            # print("use analysis result")
            # get best option from analysis            
            most_waits = 0
            ditch_card = ""
            for card, waits in possible_ditch.items():
                wait_count = 0
                for wait in waits:
                    for k, v in wait.items():
                        wait_count += v
                if wait_count >= most_waits:
                    ditch_card = card
                    most_waits = wait_count            
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
        flag = False
        for i in range(len(self.holding)):
            card = self.holding[i]
            if 'x' in card or 'X' in card:
                self.holding.pop(i)
                self.flower.append(card)
                self.draw_card(deck)
                return self.amend_flower(deck)
        return None

    def is_win(self):
        return is_win(self.holding)
    
    @_sort
    def show(self):        
        print(self.flower)
        print(self.holding)

    def discard_card(self, card):        
        try:
            id = self.holding.index(card)
            self.holding.pop(id)
        except:
            self.show()
            print("Error, No card as ", card, " in holding")            

    def see(self, card, player=None):
        self.holding.sort()
        self.saw_card = card
        self.tracker[card] -= 1

        is_upstream_player = True

        if player:
            is_upstream_player = (self.index + 3) % 4 == player.index        
        
        if card in self.holding:
            card_sum = dict()
            for c in self.holding:
                card_sum[c] = 0
            for c in self.holding:
                card_sum[c] += 1

            if card_sum[card] >= 2:
                self.can_pon = True
            if card_sum[card] == 3:
                self.can_gan = True
        
        possible_eat = list()
        if card in Deck().l_list or card in Deck().m_list or card in Deck().o_list:
            neighbor_card = get_neighbor(card)            
            self.holding.append(card)
            for i in range(len(neighbor_card)-2):
                if neighbor_card[i] in self.holding and \
                neighbor_card[i+1] in self.holding and \
                neighbor_card[i+2] in self.holding:
                    possible_eat.append(neighbor_card[i:i+3])                           
                    self.can_eat = is_upstream_player
            
            self.holding.remove(card)
            print(possible_eat)

        if card in self.listen():
            self.can_win = True


    def listen(self):
        if self.is_win():
            return None
        self.holding.sort()
        ret = list()
        for card in Deck.unique_card:
            self.holding.append(card)
            if(self.is_win()):
                ret.append(card)
            self.discard_card(card)
        return ret   
    
    def analyze(self)->Dict[str,List[Dict[str,int]]]:
        self.holding.sort()
        if self.is_win():
            return 
        else:
            ret = dict()
            tmp_holding = self.holding
            for card in tmp_holding:
                self.holding.remove(card)
                listen_cards = self.listen()
                if len(listen_cards) > 0:
                    ret_ = list()
                    for lis in listen_cards:
                        ret_.append({lis:self.tracker[lis]})
                    ret[card] = ret_
                self.holding.append(card)

            return ret


if __name__ == "__main__":
    
    stan = Player()

    stan.set_is_owner(5)

    test = ['o2', 'o3', 'l3', 'l3', 'l3', 'm5', 'm6', 'Fa', 'Fa', 'S', 'S', 'S', 'W', 'W', 'W', 'o4', 'o5', 'o6', 'x1', 'X4']

    for card in test:
        stan.draw_card(card=card)

    stan.amend_flower()

    stan.see("o4")

    stan.pon("W")

    pass
        




