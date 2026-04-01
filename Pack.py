#import Sim
#import random

#packs are randomly constructed with 13 random cards
#each card has an equal chance to be any color
#packs are not guarenteed to have an equal split of cards
class Pack:

    def __init__(self,sim):
        self.sim = sim
        self.generate_pack()
        #print(self.contents)

    def print_contents(self):
        for c in self.contents:
            print(c)

    def generate_pack(self):
        #each pack has 2 cards of each color + 3 random
        colors = ["W","U","B","R","G"]
        self.contents = [colors[self.sim.getRNG().randint(0,4)]
            for i in range(3)]
        for i in range(10):
            self.contents.append(colors[i%5])

    def pick(self,index,p=False):
        if p:
            print(f"contents = {self.contents}")
        temp = self.contents.pop(index)
        if p:
            print(f"new contents = {self.contents}")
        #print(f"temp = {temp}")
        return temp

    def at(self,index):
        return self.contents[index]

    def get_size(self):
        return len(self.contents)
