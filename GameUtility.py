from Basics import *

class PlayerRecords():
    def __init__(self, players:Players)->None:        
        self.__players = [player.index for player in players ]
        self.__wins = [0,0,0,0]
        self.__lose = [0,0,0,0]
        self.__self_draw = [0,0,0,0]
        self.__tais = [0,0,0,0]
        self.__listen = [0,0,0,0]
        return
    
    def get_wins(self):
        return self.__wins
    
    def get_lose(self):
        return self.__lose

    def get_self_draw(self):
        return self.__self_draw
    
    def get_tais(self):
        return self.__tais

    def get_listen(self):
        return self.__listen
    
    def get_index(self, player:Player)->int:
        return self.__players.index(player.index)

    def add_wins(self, player:Player):
        self.__wins[self.get_index(player)] += 1

    def add_lose(self, player:Player):
        self.__lose[self.get_index(player)] += 1

    def add_self_draw(self, player:Player):
        self.__self_draw[self.get_index(player)] += 1

    def add_listen(self, player:Player):
        self.__listen[self.get_index(player)] += 1

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
        self.players = players
        self.records = list()

    def find_owner_id(self, players:Players)->Tuple[int, int]:
        for player in players:
            if player.is_owner() >= 0:
                return player, player.is_owner()
                               
    def record(self, wind:Winds, dice:int, won_player, act_player):
        ret = ""
        self.wind.append(wind.current())
        ret += "\ncurrent wind: " + wind.current()
        owner_player, owner = self.find_owner_id(self.players)
                
        ret += "\nowner: " + str(owner_player.index) + ", streak: " + str(owner)
        self.dice.append(dice)
        ret += "\ndice rolled: " + str(dice)

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

        for player in self.players:
            if player.is_win():
                self.player_records.add_listen(player)
            elif player.is_listen():
                self.player_records.add_listen(player)

        ret += "\n" + self.player_records.to_string()
        ret+="\n"

        self.records.append(ret)
        return ret



