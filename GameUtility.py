from Basics import *

class PlayerRecords():
    def __init__(self, players:Players)->None:        
        self.__players = [player.index for player in players ]
        self.__wins = [0,0,0,0]
        self.__lose = [0,0,0,0]
        self.__self_draw = [0,0,0,0]
        self.__tais = [0,0,0,0]
        return
    
    def get_index(self, player:Player)->int:
        return self.__players.index(player.index)

    def add_wins(self, player:Player):
        self.__wins[self.get_index(player)] += 1

    def add_lose(self, player:Player):
        self.__lose[self.get_index(player)] += 1

    def add_self_draw(self, player:Player):
        self.__self_draw[self.get_index(player)] += 1

    def add_tais(self, player:Player, tai:int):
        self.__tais[self.get_index(player)] += tai

    def to_string(self)->str:
        ret = ""
        for id in self.__players:
            ret += "player index = " + str(id) + "\n"
            ret += "win = \t\t" + str(self.__wins[id]) + "\n"
            ret += "lose = \t\t" + str(self.__lose[id]) + "\n"
            ret += "self_draw = \t" + str(self.__self_draw[id]) + "\n"
            ret += "tai = \t\t" + str(self.__tais[id]) + "\n"
        return ret

class GameReport():
    def __init__(self, players:Players) -> None:
        self.wind = list()
        self.dice = list()        
        self.player_records = PlayerRecords(players) 

    def find_owner_id(self, players:Players)->Tuple[int, int]:
        for player in players:
            if player.is_owner() >= 0:
                return player.index, player.is_owner()
                               
    def record(self, wind:Winds, dice:int, players:Players):
        ret = ""
        self.wind.append(wind.current())
        ret += "\ncurrent wind: " + wind.current()
        owner_index, owner = self.find_owner_id(players)
        ret += "\nowner: " + str(owner_index) + ", streak: " + str(owner)
        self.dice.append(dice)
        ret += "\ndice rolled: " + str(dice)

        won_player = None
        act_player = players.current()        
        for player in players:
            if player.is_win():
                won_player = player
                break
        if won_player is None:
            ret += "\nno one won.\n"            
        else:
            if act_player.index == won_player.index:
                ret += "\nwinner: " + str(won_player.index) + ", self-draw"
                self.player_records.add_wins(won_player)
                self.player_records.add_self_draw(won_player)
            else:
                ret += "\nwinner: " + str(won_player.index) + ", loser: " + str(act_player.index)
                self.player_records.add_wins(won_player)
                self.player_records.add_lose(act_player)

        ret += "\n" + self.player_records.to_string()
        ret+="\n"
        return ret


