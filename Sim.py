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
