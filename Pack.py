#import Sim
#import random
import numpy as np

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
        contents = [colors[self.sim.getRNG().randint(0,4)]
            for i in range(3)]
        for i in range(10):
            contents.append(colors[i%5])
        #I have a 13 card pack and want to randomize it
        self.contents = []
        while len(contents) > 0:
            t = contents.pop(self.sim.getRNG().randint(0,len(contents)-1))
            self.contents.append(t)

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

    def get_id(self):
        return self.id

    def get_most_color(self):
        c = {'W':0,'U':0,'B':0,'R':0,'G':0}
        for i in self.contents:
            c[i] +=1
        maxColors = ['W']
        for i in c.keys():
            if i=='W':
                continue
            if c[i] > c[maxColors[0]]:
                maxColors = [i]
            elif c[i] == c[maxColors[0]]:
                maxColors.append(i)
        return maxColors
