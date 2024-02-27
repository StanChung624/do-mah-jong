
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
        self.crrnt_id = 0 # range from 0-3        
        self.game_count = 0
        self.winds = Winds()        
        self._log = ""
        self.game_report = None
        pass

    def register_a_player(self, player:Player):
        if len(self.players) < 4:            
            self.players.append(player)

    def register_deck(self, deck:Deck):
        self.deck=deck

    def __others_self_check(self, card, players:Players):
        """
            return the last action player's id.
        """

        others  = players.others()

        for other in others:
            other.see(card=card, player=players.current())
        
        others.reverse()
        for other in others:
            action = other.action()
            if action:
                if other.is_win():
                    return players                
                players.reset(other)

                self.log("player index = "+ str(other.index) + ", " + action)
                card = other.ditch()
                self.log("player index = "+ str(other.index) + ", ditch: "+ card )
                return self.__others_self_check(card, players)
                
        return players
    
    def log(self, message:str, player:Player=None, end:str="\n"):
        new_message = message + end        
        if player:
            new_message += player.show(announce=False) + end
        self._log += new_message

    
    def record(self, wind:Winds, dice:int, players:Players):
        if self.game_report is None:
            self.game_report = GameReport(self.players)        
        record = self.game_report.record(wind, dice, players)
        self.log(record)
        print(record)
        return

    def start(self):
        for player in self.players:
            player.reset()        
            player.deck = self.deck

        count = 0
        self.log("game start:")        
        
        players = Players(self.players, start_index=self.crrnt_id)        

        dice_point = self.deck.roll_dice()
        self.log("roll dice: " + str(dice_point))

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
                self.record(self.winds, dice_point, players)
                return
            count += 1

            self.log("card drawn count = " + str(count))
            self.log("player index = " + str(player.index) + ", draw: " + card)

            player.amend_flower()

            self.log("", player=player)

            if player.is_win():
                self.log("player index = "+ str(player.index) + ", win by self-draw", player=player)
                self.record(self.winds, dice_point, players)
                return
            
            card = player.ditch()

            self.log("player index = "+ str(player.index) + ", ditch: " + card)

            players = self.__others_self_check(card, players)
            player = players.current()
            for player in players:
                if player.is_win():
                    self.log("player index = "+ str(player.index) + ", win", player=player)
                    self.record(self.winds, dice_point, players)
                    return

            players.next()


            

        

if __name__ == "__main__":
    game = GameControl(debug=True)
    
    game.register_deck(Deck())

    game.register_a_player(COMPlayer(is_owner=0, index=0))
    game.register_a_player(COMPlayer(is_owner=-1, index=1))
    game.register_a_player(COMPlayer(is_owner=-1, index=2))
    game.register_a_player(COMPlayer(is_owner=-1, index=3))

    game.start()


    
