from Deck import Deck
from CheckUtility import *

class Player():
    def __init__(self, holding:list=None, is_owner:int=-1, index:int=0) -> None:
        # card tracker by player
        self.tracker = dict()
        for card in Deck.unique_card:
            self.tracker[card] = 4

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
        
    def is_owner(self)->int:
        return self.is_owner
    
    def set_is_owner(self, is_owner:int)->None:
        self.is_owner = is_owner

    def draw_card(self, deck:Deck=None, card:str=None):
        if deck:
            card = deck.serve()
            self.holding.append(card)
            self.tracker[card] -= 1
            return card
        elif card:
            self.holding.append(card)
            self.tracker[card] -= 1
            return card

    def sort_card(self):
        self.holding.sort()

    def grade(self):
        ret = dict()
        for card in self.holding:
            ret[card] = -1

        # for duplicated cards
        for card in self.holding:
            ret[card]+=1

        for card in self.holding:
            neighbor_cards = get_neighbor(card)
            if neighbor_cards:
                for nei in neighbor_cards:
                    if nei in ret.keys():
                        ret[card] += 1
                        ret[nei] += 1

        print(ret)

    def amend_flower(self, deck:Deck):
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
    
    def show(self):
        self.holding.sort()
        print(self.flower)
        print(self.holding)

    def discard_card(self, card):        
        if card in self.holding:
            id = self.holding.index(card)
            self.holding.pop(id)
        else:
            print("Error, No card as ", card, " in holding")

    def see(self, card, player):
        self.tracker[card] -= 1
        is_upstream_player = (self.index + 3) % 4 == player.index
        print(is_upstream_player)

    def listen(self):
        ret = list()
        for card in Deck.unique_card:
            self.holding.append(card)
            if(self.is_win()):
                ret.append(card)
            self.discard_card(card)
        return ret   
    
    def analyze(self):
        if self.is_win():
            return 
        else:
            ret = dict()
            for card in self.holding:
                self.discard_card(card)
                listen_cards = self.listen()
                if len(listen_cards) > 0:
                    ret_ = list()
                    for lis in listen_cards:
                        ret_.append({lis:self.tracker[lis]})
                    ret[card] = ret_
                self.holding.append(card)

            return ret


if __name__ == "__main__":
    deck = Deck()
    player = Player()

    # start
    for i in range(16):
        player.draw_card(deck=deck)

    player.amend_flower(deck)

    player.sort_card()
    player.show()

    player.grade()


