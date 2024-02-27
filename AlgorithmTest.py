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
    win_count = game.game_report.player_records.get_wins()
    lose_count = game.game_report.player_records.get_lose()
    return count, win_count, lose_count

def task(total_game):
    win_board = [0,0,0,0]
    lose_board = [0,0,0,0]

    def accum(win, lose):
        for i in range(4):
            win_board[i] += win[i]
            lose_board[i] += lose[i]
    
    avg_round = 0
    for i in range(total_game):
        round, win, lose = run_auto_game()
        accum(win, lose)        
        avg_round += round

    avg_round /= total_game

    return win_board, lose_board, avg_round

if __name__ == "__main__":

    total_game_num = 1000
    processor_num = 10
    process_game_num = int(total_game_num/processor_num)

    pool = Pool(processor_num)
    inputs = [process_game_num]*processor_num
    
    results = pool.map(func=task, iterable=inputs)    

    win_board = [0,0,0,0]
    lose_board = [0,0,0,0]
    win = 0
    lose = 0

    avg_round = 0
    for result in results:
        for i in range(4):
            win_board[i] += result[0][i]
            lose_board[i] += result[1][i]
            win += result[0][i]
            lose += result[1][i]
        avg_round += result[2] / processor_num

    print("finished game chance:", win/total_game_num * 100,"%")
    print("average rounds ", avg_round)
    
    print("lose rate:", lose/total_game_num * 100,"%")
    
    for i in range(4):
        print("player", i+1, "won", win_board[i], "games, with win rate ", win_board[i]/total_game_num * 100, "%")        
        
    