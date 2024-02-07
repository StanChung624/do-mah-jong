from tqdm import tqdm
from Deck import Deck
from Player import Player
from CheckUtility import *

class Expert():
    rules = dict(PongPong = 4,
                 BigFour = 8,
                 BigThree = 8,
                 SmallFour = 4,
                 SmallThree = 4)

    def score_board(self):
        return dict(flower=0,
                   E=0,S=0,W=0,N=0,
                   Ch=0,Fa=0,By=0,
                   Pong=0, Stt=0)
        
    def count_tai(self, player:Player):
        player.holding.sort()
        holding = player.holding
        combinations = comb_remove_pair(holding)
        for comb in combinations:
            
            score = self.score_board()

            # record pair
            if comb[-1] in score.keys():
                score[comb[-1]] = 0.5

            # record txt
            no_pair = comb[:-2]
            no_pair_n_txt, txt_count = check_txt(no_pair)

            if not no_pair_n_txt:
                continue

            if txt_count:
                for txt, count in txt_count.items():
                    if count >= 3:
                        score[txt] = 1

            result, score["Pong"] = check_id(no_pair_n_txt, "o", score["Pong"])
            if not result:
                continue

            result, score["Pong"] = check_id(no_pair_n_txt, "l", score["Pong"])
            if not result:
                continue

            result, score["Pong"] = check_id(no_pair_n_txt, "m", score["Pong"])
            if not result:
                continue
            
            score["Stt"] = 5 - score["Pong"]
            break

        print(score)
            
if __name__ == "__main__":
    win = 0
    count = 0
    for i in tqdm(range(1000000)):
        count +=1

        deck = Deck()
        stan = Player(-1)
        for i in range(16):
            stan.draw_card(deck)

        stan.amend_flower(deck)
        stan.sort_card()
        
        listen_card = stan.listen()

        if(listen_card):            
            stan.show()
            win += 1
            print(listen_card)
            print(win/count*100, "%")
            stan.holding.append(listen_card[0])
            Expert().count_tai(stan)

    

    
