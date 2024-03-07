from do_mah_jong.Basic import *
from do_mah_jong.COMStyle.COMStyle import *
from multiprocessing import Pool


def run_auto_game():
    game = GameControl()
    game.register_a_player(player=COMPlayer(is_owner=0, index=2, strategy=Coward))
    game.register_a_player(player=COMPlayer(is_owner=-1, index=3, strategy=PoPo))
    game.register_a_player(player=COMPlayer(is_owner=-1, index=1))
    game.register_a_player(player=COMPlayer(is_owner=-1, index=0))
    game.register_deck(Deck())

    count = game.start()
    win_count = game.game_report.player_records.get_wins()
    lose_count = game.game_report.player_records.get_lose()
    self_draw_count = game.game_report.player_records.get_self_draw()
    listen_count = game.game_report.player_records.get_listen()
    return count, win_count, lose_count, self_draw_count, listen_count

def task(total_game):
    win_board = [0,0,0,0]
    lose_board = [0,0,0,0]
    self_draw_board = [0,0,0,0]
    listen_board = [0,0,0,0]


    def accum(win, lose, self_draw, listen):
        for i in range(4):
            win_board[i] += win[i]
            lose_board[i] += lose[i]
            self_draw_board[i] += self_draw[i]
            listen_board[i] += listen[i]
    
    avg_round = 0
    for i in range(total_game):
        round, win, lose, self_draw, listen = run_auto_game()
        accum(win, lose, self_draw, listen)        
        avg_round += round

    avg_round /= total_game

    return win_board, lose_board, self_draw_board, listen_board, avg_round

if __name__ == "__main__":

    total_game_num = 1024
    processor_num = 16
    process_game_num = int(total_game_num/processor_num)

    pool = Pool(processor_num)
    inputs = [process_game_num]*processor_num
    
    results = pool.map(func=task, iterable=inputs)    

    win_board = [0,0,0,0]
    lose_board = [0,0,0,0]
    self_draw_board = [0,0,0,0]
    listen_board = [0,0,0,0]
    win = 0
    lose = 0

    avg_round = 0
    for result in results:
        for i in range(4):
            win_board[i] += result[0][i]
            lose_board[i] += result[1][i]
            self_draw_board[i] += result[2][i]
            listen_board[i] += result[3][i]
            win += result[0][i]
            lose += result[1][i]
        avg_round += result[4] / processor_num

    print("finished game chance:", win/total_game_num * 100,"%")
    print("average rounds ", avg_round)
    
    print("lose rate:", lose/total_game_num * 100,"%")
    
    for i in range(4):
        print("player", i)
        print("\twon      ", win_board[i], "games, with win rate \t", win_board[i]/total_game_num * 100, "%")
        print("\tlose     ", lose_board[i], "games, with lose rate \t", lose_board[i]/total_game_num * 100, "%")
        print("\tself-draw", self_draw_board[i], "games, with s-draw rate \t", self_draw_board[i]/total_game_num * 100, "%")
        print("\tlisten   ", listen_board[i], "games, with rate \t\t", listen_board[i]/total_game_num * 100, "%")
        
    