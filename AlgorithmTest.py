from COMPlayer import COMPlayer
from GameController import GameControl, Deck
from multiprocessing import Pool


def run_auto_game():
    game = GameControl()
    game.register_a_player(player=COMPlayer(is_owner=0, index=0))
    game.register_a_player(player=COMPlayer(is_owner=-1, index=1))
    game.register_a_player(player=COMPlayer(is_owner=-1, index=2))
    game.register_a_player(player=COMPlayer(is_owner=-1, index=3))
    game.register_deck(Deck())

    count = game.start()    
    score_board = game.game_report.player_records.get_wins()
    return count, score_board

def task(total_game):
    score_board = [0,0,0,0]

    def accum(input_list):
        for i in range(4):
            score_board[i] += input_list[i]
    
    avg_round = 0
    for i in range(total_game):
        round, wins = run_auto_game()
        accum(wins)
        avg_round += round

    avg_round /= total_game

    return score_board, avg_round

if __name__ == "__main__":

    total_game_num = 40
    processor_num = 4
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