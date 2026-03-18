#import random
#import Player
#from Pack import Pack
from Sim import Sim
from Filter import Filter

me = Filter()
sim = Sim(18,1,me)


sim.print_pool()

sim.run_sim()
