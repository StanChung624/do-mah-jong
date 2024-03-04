import random
from typing import List
class Deck():
    m_list = ["m1","m2","m3","m4","m5","m6","m7","m8","m9"]
    o_list = ["o1","o2","o3","o4","o5","o6","o7","o8","o9"]
    l_list = ["l1","l2","l3","l4","l5","l6","l7","l8","l9"]
    t_list = ["E","S","W","N","Ch","Fa","By"]
    f_list = ["x1","x2","x3","x4","X1","X2","X3","X4"]
    unique_card = m_list + o_list + l_list + t_list

    def __init__(self):
        self.deck_tracker = dict()
        self.seq = list()
        self.sea = list()
        self.shuffle_deck()

    def shuffle_deck(self):
        for card in self.m_list:
            self.deck_tracker[card] = 4
            self.seq.extend([card]*4)
        
        for card in self.o_list:
            self.deck_tracker[card] = 4
            self.seq.extend([card]*4)

        for card in self.l_list:
            self.deck_tracker[card] = 4
            self.seq.extend([card]*4)

        for card in self.t_list:
            self.deck_tracker[card] = 4
            self.seq.extend([card]*4)

        for card in self.f_list:
            self.deck_tracker[card] = 1
            self.seq.append(card)

        random.shuffle(self.seq)

        for i in range(16):
            self.sea.append(self.seq.pop(len(self.seq)-1-i))

    def roll_dice(self)->int:
        return random.randint(a=3, b=18)
 

    def remain_number(self)->int:
        count = 0
        for card in self.deck_tracker.keys():
            count += self.deck_tracker[card]
        return count
    
    def get_seq(self):
        return self.seq
    
    def serve(self)->str:
        if len(self.seq) == 0:            
            return None
        self.deck_tracker[self.seq[0]] -= 1        
        return self.seq.pop(0)

def is_text(card:str)->bool:
    if card in Deck.t_list or card in Deck.f_list:
        return True
    else:
        return False
    
def translate(card:str)->str:
    t_map = {"Ch":"中", "Fa":"發", "By":"白", "E":"東", "S":"南", "W":"西", "N":"北"}
    map = {"o":"筒", "l":"條", "m":"萬"}       
    f_map = {"x1":"春1","x2":"夏2","x3":"秋3","x4":"冬4","X1":"梅1","X2":"蘭2","X3":"菊3","X4":"竹4"}
    ret = card
    try:
        if card in Deck.t_list:
            ret = t_map[card]
        elif not is_text(card):
            ret = str(card[1]) + map[card[0]]
        elif card in f_map.keys():
            ret = f_map[card]
        return ret
    except:
        return card

def translate_list(cards:List[str])->List[str]:
    ret = list()
    for card in cards:
        ret.append(translate(card))
    return ret
    
class CustomDeck(Deck):
    def __init__(self):
        super().__init__()        
        print(self.seq)
        print(self.sea)

if (__name__=="__main__"):
    deck = Deck()
    count_flower = 0
    for i in range(64):
        card = deck.serve()
        if "x" in card or "X" in card:
            count_flower += 1
            
    print(count_flower)
    print(len(deck.sea))
    