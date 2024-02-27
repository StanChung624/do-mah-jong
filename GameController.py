
from Deck import Deck
from Player import Player
from COMPlayer import COMPlayer
from MANPlayer import MANPlayer
from Basics import *
from GameUtility import *

class GameControl():
    def __init__(self, debug:bool=False) -> None:
        self.players = list()
        self.deck = Deck()
        self.debug = debug
        self.crrnt_id = FourIndexBase()
        self.game_count = 0
        self.winds = Winds()        
        self._log = ""
        self.game_report = None
        self.__is_full_round = False
        pass

    def register_a_player(self, player:Player):
        if len(self.players) < 4:            
            self.players.append(player)        

    def register_deck(self, deck:Deck):
        self.deck=deck

    def __others_self_check(self, card, players:Players, announce:bool=False):
        """
            return the players and last action player
        """

        others  = players.others()

        for other in others:
            other.see(card=card, player=players.current())
        
        others.reverse()
        for other in others:
            action = other.action()
            if action:
                if other.is_win():
                    return players, players.current()
                
                players.reset(other)

                self.log("player index = "+ str(other.index) + ", " + action,
                          announce=announce)
                card = other.ditch()
                self.log("player index = "+ str(other.index) + ", ditch: "+ card,
                          announce=announce)
                return self.__others_self_check(card, players, announce=announce)
                
        return players, players.current()
    
    def log(self, message:str, player:Player=None, end:str="\n", announce:bool=False):
        new_message = message + end        
        if player:
            new_message += player.show(announce=False) + end
        self._log += new_message
        if announce:
            print(new_message)

    
    def record(self, wind:Winds, dice:int, won_player:Player, act_player:Player):
        if self.game_report is None:
            self.game_report = GameReport(self.players)
        record = self.game_report.record(wind, dice, won_player, act_player)
        self.log(record)
        return
    
    def __environment_update(self):
        win = -1
        for i in range(4):
            player = self.players[i]
            if player.is_win():
                win = i
        owner = self.crrnt_id.current_id()            
                
        if win == owner or win < 0:
            self.players[owner].owner += 1
            self.__is_full_round = False
            return 
        
        else:
            self.crrnt_id.next()
            non_owner = [0,1,2,3]
            non_owner.remove(self.crrnt_id.current_id())
            for i in non_owner:
                self.players[i].owner = -1
            self.players[self.crrnt_id.current_id()].owner = 0

            if self.crrnt_id.current_id() == 0:
                self.winds.next()
        
        if self.winds.current() == "E" and self.crrnt_id.current_id() == 0:            
            self.__is_full_round = True
        else:
            self.__is_full_round = False
    
    def is_full_round(self):
        return self.__is_full_round

    def start(self, announce:bool=False):
        for player in self.players:
            player.reset()        
            player.deck = self.deck

        count = 0
        self.log("game start:", announce=announce)
        
        players = Players(self.players, start_index=self.crrnt_id.current_id())        

        dice_point = self.deck.roll_dice()
        self.log("roll dice: " + str(dice_point), announce=announce)

        #deal cards
        for grab_i in range(4):
            for player in players:
                for card_i in range(4):
                    player.draw_card()                 

        self.log("\ncard dealed")
        for player in players:            
            self.log("", player=player)

        #amend flowers
        for player in players:
            player.amend_flower()

        self.log("flower amended")
        for player in players:
            self.log("", player=player)

        while True:
            player = players.current()

            card = player.draw_card()
            if card is None:
                self.record(self.winds, dice_point, None, player)
                self.__environment_update()
                return count
            count += 1

            self.log("card drawn count = " + str(count), announce=announce)
            self.log("player index = " + str(player.index) + ", draw: " + card)

            player.amend_flower()

            self.log("", player=player)

            if player.is_win():
                self.log("player index = "+ str(player.index) + ", win by self-draw",
                          player=player, announce=announce)
                self.record(self.winds, dice_point, won_player=player, act_player=player)
                self.__environment_update()
                return count
            
            card = player.ditch()

            self.log("player index = "+ str(player.index) + ", ditch: " + card,
                      announce=announce)

            players, act_player = self.__others_self_check(card, players, announce=announce)            
            for player in players:
                if player.is_win():
                    self.log("player index = "+ str(player.index) + ", win", player=player,
                             announce=announce)                    
                    self.record(self.winds, dice_point, won_player=player, act_player=act_player)
                    self.__environment_update()
                    return count

            players.next()


            

        

if __name__ == "__main__":
    game = GameControl(debug=True)    

    game.register_a_player(COMPlayer(is_owner=0, index=0))
    game.register_a_player(COMPlayer(is_owner=-1, index=1))
    game.register_a_player(COMPlayer(is_owner=-1, index=2))
    game.register_a_player(COMPlayer(is_owner=-1, index=3))
    
    while True:
        game.register_deck(Deck())
        game.start(announce=False)
        print(game.game_report.records[-1])
        if game.is_full_round():
            break



    
