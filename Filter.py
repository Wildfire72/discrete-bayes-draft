#import random
from Player import Player
#import Pack
#import Sim

class Filter(Player):
    
    def __init__(self):
        self.pool = []
        self.color_combo=["U","B"]
        self.p=False

    def pick_card(self,pack):
        #self.pool.append(pack.pick(0))
        super().pick_card(pack)

    def print_pool(self):
        pool = self.get_pool()
        d = {"W":0,"U":0,"B":0,"R":0,"G":0}
        for c in pool:
            d[c]+=1
        cc = self.get_color_combo()
        print(f"Filter's color combo: {cc[0]}{cc[1]}")
        print(f"Pool size: {len(self.get_pool())}")
        print(f"W:{d['W']}, U:{d['U']}, B:{d['B']}, R:{d['R']}, G:{d['G']}")
