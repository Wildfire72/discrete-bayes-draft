#import Sim
#import random

#packs are randomly constructed with 13 random cards
#each card has an equal chance to be any color
#packs are not guarenteed to have an equal split of cards
class Pack:

    def __init__(self,sim):
        self.sim = sim
        self.generate_pack()

    def print_contents(self):
        for c in self.contents:
            print(c)

    def generate_pack(self):
        colors = ["W","U","B","R","G"]
        self.contents = [colors[self.sim.getRNG().randint(0,4)]
            for i in range(13)]

    def pick(self,index):
        return self.contents.pop(index)
