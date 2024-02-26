from COMPlayer import *
from multiprocessing import Pool


def run_auto_game(score_board:list=None)->int:
    """
    if the game is out of deck or not.
    """
    deck = Deck()

    players = [COMPlayer(index=0, is_owner= 0, deck=deck),\
            COMPlayer(index=1, is_owner=-1, deck=deck),\
            COMPlayer(index=2, is_owner=-1, deck=deck),\
            COMPlayer(index=3, is_owner=-1, deck=deck)]

    for i in range(4):
        for id in range(4):        
            for j in range(4):
                players[id].draw_card() 


    # amend flower
    for i in range(4):
        players[i].amend_flower()

    id = 0
    round = 0

    to_stop = False
    while not to_stop:
        if id ==0:
            round += 1
        if not players[id].draw_card(announce=False):
            # print("no body win..")
            to_stop = True            
            return round
            break

        players[id].amend_flower()

        if players[id].is_win():
            is_stop = True
            if score_board:
                score_board[id] += 1
            # print("win!")
            # players[id].show()
            return round
            break

        card = players[id].ditch()
        def others_check(card, current_player_id)->Tuple[int, bool]:
                """
                return next player's id and if someone has won
                """
                # print("player", current_player_id, "ditch", card)
                other_ids = [0,1,2,3]
                other_ids.remove(current_player_id)

                for other in other_ids:
                    players[other].see(card=card, player=players[current_player_id])
                
                other_ids.reverse()
                for other in other_ids:
                    if players[other].action(announce=False):
                        # print("Player", other)

                        if players[other].is_win():
                            # print("win!")                            
                            return other, True
                        
                        current_player_id = other
                        return others_check(players[other].ditch(), current_player_id)
                        
                return current_player_id, False

        id, to_stop = others_check(card, id)    
        if to_stop:
            score_board[id] += 1
            return round
            
        id += 1
        id %= 4

def task(total_game):
    score_board=[0,0,0,0]
    avg_round = 0
    for i in range(total_game):
        avg_round += run_auto_game(score_board=score_board) / total_game
            
    return score_board, avg_round

if __name__ == "__main__":

    total_game_num = 1000
    processor_num = 10
    process_game_num = int(total_game_num/processor_num)

    pool = Pool(processor_num)
    inputs = [process_game_num]*processor_num
    
    results = pool.map(func=task, iterable=inputs)    

    score_board = [0,0,0,0]
    win = 0

    avg_round = 0
    for result in results:
        for i in range(4):
            score_board[i] += result[0][i]
            win += result[0][i]
        avg_round += result[1] / processor_num

    print("finished game chance:", win/total_game_num * 100,"%")
    print("average rounds ", avg_round)
    p = 0
    for i in score_board:
        print("player", p, "won", i, "games, with win rate ", i/total_game_num * 100, "%")
        p+=1