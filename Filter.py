#import random
from Player import Player
#import Pack
#import Sim
import numpy as np

class Filter(Player):
    
    def __init__(self):
        self.pool = []
        self.color_combo=["U","B"]
        self.p=False
        self.prev = [0.2,0.2,0.2,0.2,0.2] #start with uniform belief
        self.bels = {}
        self.index = 0

    def pick_card(self,pack):
        #self.pool.append(pack.pick(0))
        self.filter(pack)
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

    def get_motion(self,bin_num):
        l = [0.15 for i in range(5)]
        l[bin_num] = 0.4
        return l

    def get_likelihood(self,pack):
        colors = pack.get_most_color()
        const = 1/pack.get_size()
        likelihood = [max(1/2 - const,0) for i in range(5)]
        if 'W' in colors:
            likelihood[0] = min(1/2+const,1)
        if 'U' in colors:
            likelihood[1] = min(1/2+const,1)
        if 'B' in colors:
            likelihood[2] = min(1/2+const,1)
        if 'R' in colors:
            likelihood[3] = min(1/2+const,1)
        if 'G' in colors:
            likelihood[4] = min(1/2+const,1)
        return likelihood

    def predict(self):
        prev = self.prev
        bel_bar = np.zeros(5)
        for bin_num in range(5):
            motion = self.get_motion(bin_num)
            for i in range(5):
                bel_bar[i] += motion[i] * prev[bin_num]
        return bel_bar

    def update(self,bel_bar,pack):
        bel_tilde = np.empty(5)
        likelihood = self.get_likelihood(pack)
        for i in range(5):
            bel_tilde[i] = bel_bar[i] * likelihood[i]
        sum = 0
        for i in bel_tilde:
            sum+=i
        bel = np.empty(5)
        for i in range(5):
            bel[i] = bel_tilde[i] / sum
        return bel

    def filter(self,pack):
        bel_bar = self.predict()
        bel = self.update(bel_bar,pack)
        self.prev = bel
        #print(f"bel = {bel}")
        self.bels[self.index] = bel
        self.index += 1

    def get_filter(self):
        whites = []
        blues = []
        blacks = []
        reds = []
        greens = []
        for i in range(39):
            step = self.bels[i]
            #print(f"step = {step}")
            whites.append(step[0])
            blues.append(step[1])
            blacks.append(step[2])
            reds.append(step[3])
            greens.append(step[4])
        return whites,blues,blacks,reds,greens
            
        
