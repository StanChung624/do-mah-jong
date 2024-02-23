import random

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

    def remain_number(self)->int:
        count = 0
        for card in self.deck_tracker.keys():
            count += self.deck_tracker[card]
        return count
    
    def get_seq(self):
        return self.seq
    
    def serve(self)->str:
        if len(self.seq) == 0:
            print("[error] deck out of cards!")
            return None
        self.deck_tracker[self.seq[0]] -= 1        
        return self.seq.pop(0)


if (__name__=="__main__"):
    deck = Deck()
    count_flower = 0
    for i in range(64):
        card = deck.serve()
        if "x" in card or "X" in card:
            count_flower += 1
            
    print(count_flower)
    print(len(deck.sea))
    