import random
from Player import Player
from Pack import Pack
#import Filter

class Sim:

    def __init__(self,seed,numOpponents,me):
        self.random = random.Random(seed)
        self.makePlayList(me,numOpponents)
        self.generateStartingPool()

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
        for i in range(1): # a draft is 3 rounds
            self.run_round()
            if i <2:
                self.generateStartingPool()
        self.print_player_pools()

    def run_round(self):
        offset = 0
        while self.pool[0].get_size() > 0:
            offset %= len(self.players)
            for i in range(len(self.players)):
                p = self.players[i]
                p.pick_card(self.pool[(i+offset)%len(self.players)])

    def print_player_pools(self):
        for p in self.players:
            p.print_pool()
            
