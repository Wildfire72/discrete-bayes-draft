#players will randomly select a color combo to draft
#import Sim
#import Pack
#import random

class Player:

    def __init__(self,sim):
        self.sim = sim
        self.pick_color_pair()
        self.pool = []
        self.p=False

    def get_pool(self):
        return self.pool

    def get_color_combo(self):
        return self.color_combo

    def pick_color_pair(self):
        i = self.sim.getRNG().randint(0,9)
        c = ["W","U","B","R","G"]
        pairs = {0:[c[0],c[1]],1:[c[0],c[2]],2:[c[0],c[3]],3:[c[0],c[4]],
            4:[c[1],c[2]],5:[c[1],c[3]],6:[c[1],c[4]],7:[c[2],c[3]],
            8:[c[2],c[4]],9:[c[3],c[4]]}
        self.color_combo = pairs[i]

    def pick_card(self,pack,pp=False):
        #print(f"Pool size: {len(self.get_pool())}")
        #see if a card matches either color in its pair
        for i in range(pack.get_size()):
            if pack.at(i) in self.color_combo:
                self.pool.append(pack.pick(i,pp))
                if self.p:
                    print(f"{self.color_combo} picked a {self.pool[-1]} card")
                    print(f"Their pool is now {self.print_pool()}")
                return
        #no cards in colors so just add the first one
        self.pool.append(pack.pick(0,pp))
        if self.p:
            print("No colors in combo left")
            print(f"Their pool is now {self.print_pool()}")
            exit(3)

    def print_pool(self):
        pool = self.get_pool()
        d = {"W":0,"U":0,"B":0,"R":0,"G":0}
        for c in pool:
            d[c]+=1
        cc = self.get_color_combo()
        print(f"Player's color combo: {cc[0]}{cc[1]}")
        print(f"Pool size: {len(self.get_pool())}")
        print(f"W:{d['W']}, U:{d['U']}, B:{d['B']}, R:{d['R']}, G:{d['G']}")
                
                  
