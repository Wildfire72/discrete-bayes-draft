import random
from Player import Player
from Pack import Pack
#import Filter

class Sim:

    def __init__(self,seed,numOpponents,me):
        self.random = random.Random(seed)
        self.makePlayList(me,numOpponents)
        self.generateStartingPool()
        self.percs = {} #percentage of the card pool at each step
        self.index = 0

    def getRNG(self):
        return self.random

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
        for i in range(3): # a draft is 3 rounds
            self.run_round()
            if i <2:
                self.generateStartingPool()
        self.print_player_pools()

    def run_round(self):
        offset = 0
        while self.pool[0].get_size() > 0:
            offset %= len(self.players)
            self.average_packs()
            for i in range(len(self.players)):
                p = self.players[i]
                p.pick_card(self.pool[(i+offset)%len(self.players)])
            offset+=1
            self.index +=1

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

    def get_averages(self):
        whites = []
        blues = []
        blacks = []
        reds = []
        greens = []
        for i in range(39):
            step = self.percs[i]
            whites.append(step[0])
            blues.append(step[1])
            blacks.append(step[2])
            reds.append(step[3])
            greens.append(step[4])
        return whites,blues,blacks,reds,greens

    def print_player_pools(self):
        for p in self.players:
            p.print_pool()

            
