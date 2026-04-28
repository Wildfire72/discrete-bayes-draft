import random
from Player import Player
from Pack import Pack
import numpy as np
#import Filter

class Sim:

    def __init__(self,seed,numOpponents,me,num_rounds,printResults=False):
        self.random = random.Random(seed)
        self.makePlayList(me,numOpponents)
        self.generateStartingPool()
        self.percs = {} #percentage of the card pool at each step
        self.index = 0
        self.bels = {}
        self.prev = [0.2,0.2,0.2,0.2,0.2] #start with uniform belief
        self.motion = self.generateMotion()
        self.num_rounds=num_rounds
        self.printResults=printResults
        #print(self.motion)

    def getRNG(self):
        return self.random

    def generateMotion(self):
        d = {"W":0,"U":0,"B":0,"R":0,"G":0}
        for player in self.players:
            for key in d.keys():
                if key in player.color_combo:
                    d[key] += 1
        base = 1/13
        motion = np.empty(5)
        total = 0
        for key in d.keys():
            total += d[key]
        st = "WUBRG"
        for i in range(5):
            motion[i] = 1 - (base + d[st[i]]/total)
        sum = 0
        for i in range(5):
            sum += motion[i]
        final_motion = np.empty(5)
        for i in range(5):
            final_motion[i] = motion[i]/sum
        return final_motion

    def get_motion(self):
        motion = self.motion.copy()
        smallest = np.min(motion) #add noise
        rand1 = self.random.uniform(0,smallest)
        rand2 = self.random.uniform(0,smallest/2)
        #print(f"smallest = {smallest}")
        #print(f"rand1 = {rand1}")
        motion[self.random.randint(0,4)] += rand1
        motion[self.random.randint(0,4)] -= rand1
        motion[self.random.randint(0,4)] += rand2
        motion[self.random.randint(0,4)] -= rand2
        return motion

    """def get_motion(self,bin_num):
        l = [0.1 for i in range(5)]
        l[bin_num] = 0.6
        return l"""

    def get_likelihood(self):
        self.average_packs()
        highest = [0]
        cur = self.percs[self.index]
        for i in range(5):
            if cur[i] > cur[highest[0]]:
                highest = [i]
            elif cur[i] == cur[highest[0]]:
                highest.append(i)
        like = np.empty(5)
        for i in range(5):
            if i in highest:
                like[i] = 0.6
            else:
                like[i] = 0.4
        return like

    def predict(self):
        prev = self.prev
        bel_bar = np.zeros(5)
        for bin_num in range(5):
            motion = self.get_motion()
            #print(f"motion is type {type(motion)}")
            for i in range(5):
                bel_bar[i] += motion[i] * prev[bin_num]
        #print(f"bel_bar is type {type(bel_bar)}")
        return bel_bar

    def update(self,bel_bar):
        bel_tilde = np.empty(5)
        likelihood = self.get_likelihood()
        for i in range(5):
            bel_tilde[i] = bel_bar[i] * likelihood[i]
        sum = 0
        for i in bel_tilde:
            sum+=i
        bel = np.empty(5)
        for i in range(5):
            bel[i] = bel_tilde[i] / sum
        return bel

    def filter(self):
        bel_bar = self.predict()
        bel = self.update(bel_bar)
        self.prev = bel
        #print(f"bel = {bel}")
        self.bels[self.index] = bel
        self.index += 1
        
    def makePlayList(self,me,numOpponents):
        self.players = [me]
        for i in range(numOpponents):
            self.players.append(Player(self))

    def generateStartingPool(self):
        self.pool = [Pack(self) for i in range(len(self.players))]

    def print_pool(self):
        for p in self.pool:
            p.print_contents()
            print("===")

    def run_sim(self):
        for i in range(self.num_rounds): # a draft is 3 rounds
            self.run_round()
            if i <2:
                self.generateStartingPool()
        if self.printResults:
            self.print_player_pools()

    def run_round(self):
        offset = 0
        while self.pool[0].get_size() > 0:
            offset %= len(self.players)
            self.filter()
            #self.get_open()
            for i in range(len(self.players)):
                p = self.players[i]
                p.pick_card(self.pool[(i+offset)%len(self.players)])
            offset+=1
            #self.index +=1

    def average_packs(self):
        total = self.pool[0].get_size()*len(self.players)
        nums = [0,0,0,0,0]
        for pack in self.pool:
            for c in pack.contents:
                if c == "W":
                    nums[0] += 1
                elif c == "U":
                    nums[1] += 1
                elif c == "B":
                    nums[2] += 1
                elif c == "R":
                    nums[3] += 1
                else:
                    nums[4] += 1
        for i in range(5):
            nums[i] /= total
        self.percs[self.index] = nums            

    def get_filter(self):
        whites = []
        blues = []
        blacks = []
        reds = []
        greens = []
        for i in range(13*self.num_rounds):
            step = self.bels[i]
            whites.append(step[0])
            blues.append(step[1])
            blacks.append(step[2])
            reds.append(step[3])
            greens.append(step[4])
        return whites,blues,blacks,reds,greens

    def print_player_pools(self):
        for p in self.players:
            p.print_pool()

            
