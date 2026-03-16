#import random
from Player import Player
#import Pack
#import Sim

class Filter(Player):
    
    def __init__(self):
        self.pool = []

    def get_color_combo(self):
        return ["U","B"]

    def pick_card(self,pack):
        self.pool.append(pack.pick(0))
