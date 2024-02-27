from typing import List, Tuple
from Player import Player

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

class Winds(FourIndexBase):
    WIND = ["E", "S", "W", "N"]

    def __init__(self, start_index:int=0):
        return super().__init__(start_index)
    
    def __next__(self):
        return Winds().WIND[super().__next__()]

    def current(self)->str:
        return Winds.WIND[self.index]

    def reset(self, index:int):
        self.index = index
    
    
    
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