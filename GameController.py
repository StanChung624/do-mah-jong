from typing import List
from Deck import Deck
from Player import Player
from COMPlayer import COMPlayer
from MANPlayer import MANPlayer

class FourIndexBase():
    def __init__(self, start_index:int=0):
        self.index = start_index
        self.max_length = 4
        self.count = 0

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):        
        if self.count < self.max_length:
            self.count += 1
            ret = self.index
            self.next()
            return ret
        else:
            raise StopIteration

    def current_id(self)->int:
        return self.index
    
    def next(self)->None:
        self.index += 1
        self.index %= 4

class Wind(FourIndexBase):
    WIND = ["E", "S", "W", "N"]
    def __next__(self):
        return Wind().WIND[super().__next__()]
    
class Players(FourIndexBase):
    def __init__(self, players:List[Player], start_index:int=0):
        self.players = players
        return super().__init__(start_index)
    
    def __next__(self):
        return self.players[super().__next__()]

    def current(self)->Player:
        return self.players[self.index]
    
    def reset(self, player:Player):
        new_index = 0
        for self_player in self.players:
            if self_player.index == player.index:
                self.index = new_index
                return
            new_index += 1
    
    def others(self, index:int=None)->List[Player]:
        if index is None:
            index = self.index            
        ret = list()
        for i in FourIndexBase(self.index):
            ret.append(self.players[i])
        ret.pop(-1)
        return ret

class GameControl():
    def __init__(self, debug:bool=False) -> None:
        self.players = list()
        self.deck = Deck()
        self.debug = debug
        self.crrnt_id = 0 # range from 0-3        
        self.game_count = 0
        self.wind = ["E", "S", "W", "N"]
        self.wind_index = 0
        self._log = ""
        pass

    def set_func(action):
        def wrapper(self, *args, **kwargs):
            announce = kwargs.setdefault("announce", self.debug)
            if announce:
                print(action.__name__, "called")
            action(self, args[0])
        return wrapper

    @set_func
    def register_a_player(self, player:Player):
        if len(self.players) < 4:            
            self.players.append(player)

    @set_func
    def register_deck(self, deck:Deck):
        self.deck=deck

    def __others_self_check(self, card, players:Players):
        """
            return the last action player's id.
        """

        others  = players.others()

        for other in others:
            other.see(card=card, player=self.players[self.crrnt_id])
        
        others.reverse()
        for other in others:
            action = other.action()
            if action:
                players.reset(other)
                if other.is_win():                    
                    return players                
                self.log("player index = "+ str(other.index) + ", " + action)
                card = other.ditch()
                self.log("player index = "+ str(other.index) + ", ditch: "+ card )
                return self.__others_self_check(card, players)
                
        return players
    
    def log(self, message:str, player:Player=None, end:str="\n"):    
        self._log += message + end
        if player:
            self._log += player.show(announce=False) + end

    def start(self):
        for player in self.players:
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
                # deck out of card
                return
            count += 1

            self.log("card drawn count = " + str(count))
            self.log("player index = " + str(player.index) + ", draw: " + card)

            player.amend_flower()

            self.log("", player=player)

            if player.is_win():
                self.log("player index = "+ str(player.index) + ", win by self-draw", player=player)
                # self draw won
                return
            
            card = player.ditch()

            self.log("player index = "+ str(player.index) + ", ditch: " + card)

            players = self.__others_self_check(card, players)
            if players.current().is_win():
                self.log("player index = "+ str(players.current().index) + ", win", player=players.current())
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

    print(game._log)

