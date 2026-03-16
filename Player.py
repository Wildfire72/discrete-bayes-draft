#players will randomly select a color combo to draft
#import Sim
#import Pack
#import random

class Player:

    def __init__(self,sim):
        self.sim = sim
        self.pick_color_pair()
        self.pool = []

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

    def pick_card(self,pack):
        #see if a card matches either color in its pair
        for i in range(len(pack)):
            if pack[i] in self.color_pair:
                self.pool.append(pack.pick(i))
                return
        #no cards in colors so just add the first one
        self.pool.append(pack.pick(0))
                
                  
