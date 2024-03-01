from typing import List, Dict
from Deck import Deck, is_text
from Player import Player
from CheckUtility import listen, get_neighbor

class COMThoughtsBase():
    def __init__(self, player:Player)->None:
        self.index = player.index
        self.holding = player.holding # current holding
        self.tracker = player.tracker # all left cards count tracker
        self.seen_cards = player.seen_cards # other opponents played card        

        self.bias_text = -2
        self.bias_side = -1

        self.grades = self.__generate_grade()
        self.count = self.__generate_count()
        self.bias = self.__generate_bias()
        self.base_add_bias()
        

    def __generate_grade(self)->Dict[str,int]:
        ret = dict()
        for card in self.holding:
            ret[card] = 0
        return ret
    
    def __generate_bias(self)->Dict[str,int]:
        ret = dict()
        for card in Deck.t_list:
            ret[card] = self.bias_text
        ret[Deck.l_list[0]] = self.bias_side * 2
        ret[Deck.l_list[-1]] = self.bias_side * 2
        ret[Deck.m_list[0]] = self.bias_side * 2
        ret[Deck.m_list[-1]] = self.bias_side * 2
        ret[Deck.o_list[0]] = self.bias_side * 2
        ret[Deck.o_list[-1]] = self.bias_side * 2
        ret[Deck.l_list[1]] = self.bias_side
        ret[Deck.l_list[-2]] = self.bias_side
        ret[Deck.m_list[1]] = self.bias_side
        ret[Deck.m_list[-2]] = self.bias_side
        ret[Deck.o_list[1]] = self.bias_side
        ret[Deck.o_list[-2]] = self.bias_side
        return ret


    def __generate_count(self)->Dict[str,int]:
        ret = dict()
        for card in self.holding:
            ret.setdefault(card, 0)
        for card in self.holding:
            ret[card] += 1
        return ret
    
    def base_add_bias(self):
        for card, count in self.count.items():
            if count == 1 and card in self.bias.keys():
                self.grades[card] += self.bias[card]
    
    def base_ditch_to_listen(self, point:int):
        for card in self.grades.keys():
            holding = list(self.holding)
            holding.remove(card)
            score = len(listen(holding)) * (-point)
            self.grades[card] += score
    
    def base_neighbor_cards(self, point:int):
        for card in self.grades.keys():
            if not is_text(card):
                neighbors = get_neighbor(card)
                for nei in neighbors:
                    if nei in self.grades.keys():
                        self.grades[card] += point

    def base_duplicate_cards(self, point:int):
        for card, count in self.count.items():
            if count > 1:
                self.grades[card] += point

    def base_down_stream_player_played_cards(self, point:int):
        down_stream_index = (self.index + 1) % 4
        for card in self.count.keys():
            card_played_times = self.seen_cards[down_stream_index][card]            
            self.grades[card] += (-point) * card_played_times
    
    def best_ditch(self)->str:
        lowest_count = 999999
        ditch_card = ""
        for card, grade in self.grades.items():
            if grade < lowest_count:
                lowest_count = grade
                ditch_card = card
        return ditch_card

    def base_discarded_cards(self, point:int):
        for card in self.holding:
            for other, tracker in self.seen_cards.items():
                self.grades[card] += tracker[card] * (-point)


    def base_discarded_series_cards(self, point:int):
        def get_series_cards(card:str):
            if is_text(card):
                return list()
            else:
                typ = card[0]
                num = int(card[1])
                nums = [num, num+3, num+6]
                ret = []
                for i in nums:
                    if i > 10:
                        i -= 9
                    ret.append(typ+str(i))
                return ret
        for _, tracker in self.seen_cards.items():
            for card, count in tracker.items():
                for crd in get_series_cards(card):
                    if crd in self.grades.keys():
                        self.grades[crd] += (-point)*count


    
if __name__ == "__main__":
    deck = ['l1', 'l2', 'l3', 'm5', 'm5', 'm6', 'm7', 'N', 'm9']
    player = Player(holding=deck)

    player.see("m2", player_index=1)
    
    thought = COMThoughtsBase(player)
    
    thought.base_discarded_series_cards(5)

    print(thought.grades)