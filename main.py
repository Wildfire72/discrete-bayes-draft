#import random
#import Player
#from Pack import Pack
from Sim import Sim
from Filter import Filter
import matplotlib.pyplot as plt
import numpy as np

num_rounds = 3
seed = 1891

#"""# <-- uncomment/comment this line to switch between single iteration and suite
seeds = np.arange(300,600)
avg_difs = np.empty(len(seeds))
for seed in range(len(seeds)):
    me = Filter(num_rounds)
    sim = Sim(seed,7,me,num_rounds)
    #sim.print_pool()
    sim.run_sim()
    w,u,b,r,g = me.get_filter()
    w1,u1,b1,r1,g1 = sim.get_filter()
    difs = np.empty(len(w))
    for i in range(len(w)):
        dif = abs(w1[i]-w[i])+abs(u1[i]-u[i])+abs(b1[i]-b[i])
        dif += abs(r1[i]-r[i])+abs(g1[i]-g[i])
        difs[i] = dif
    avg_difs[seed] = np.mean(difs)

#suite
plt.plot(seeds,avg_difs)
plt.xlabel("Seed")
plt.ylabel("Average Difference")
plt.title("Average Difference")
print(f"Total Average Difference = {np.mean(avg_difs)}")
plt.show()


""" #<-- leave this line
#single iteration
me = Filter(num_rounds)
sim = Sim(seed,7,me,num_rounds,True)
#sim.print_pool()
sim.run_sim()
    
w,u,b,r,g = me.get_filter()
w1,u1,b1,r1,g1 = sim.get_filter()
t = np.arange(0,len(w),1)

difs = np.empty(len(t))
for i in range(len(t)):
    dif = abs(w1[i]-w[i])+abs(u1[i]-u[i])+abs(b1[i]-b[i])
    dif += abs(r1[i]-r[i])+abs(g1[i]-g[i])
    difs[i] = dif
#print(f"len(w) = {len(w)}, len(t) = {len(t)}")

#for i in range(len(u1)):
#    print(f"At Pick {i}, the Filter believes black is {b[i]}% open.")

#for i in range(len(u1)):
#    print(f"At Pick {i}, black is {b1[i]}% open.")

fig, axs = plt.subplots(nrows=3, ncols=2,figsize=(11,9))
w_ax = axs[0][0]
u_ax = axs[0][1]
b_ax = axs[1][0]
r_ax = axs[1][1]
g_ax = axs[2][0]
dif_ax = axs[2][1]

w_ax.plot(t,w,color="orange",label="Predicted",linestyle="dashed")
u_ax.plot(t,u,color="blue",linestyle="dashed")
b_ax.plot(t,b,color="black",linestyle="dashed")
r_ax.plot(t,r,color="red",linestyle="dashed")
g_ax.plot(t,g,color="green",linestyle="dashed")

w_ax.plot(t,w1,color="orange",label="Real")
u_ax.plot(t,u1,color="blue")
b_ax.plot(t,b1,color="black")
r_ax.plot(t,r1,color="red")
g_ax.plot(t,g1,color="green")

dif_ax.plot(t,difs,color="lightblue")

#fig,ax = plt.subplots()
#ax.plot(t,w,color="orange",label="White")
#ax.plot(t,u,color="blue",label="Blue")
#ax.plot(t,b,color="black",label="Black")
#ax.plot(t,r,color="red",label="Red")
#ax.plot(t,g,color="green",label="Green")

#plt.title("Belief over Time")
#plt.legend()

w_ax.set_title("White Belief")
u_ax.set_title("Blue Belief")
b_ax.set_title("Black Belief")
r_ax.set_title("Red Belief")
g_ax.set_title("Green Belief")
dif_ax.set_title("Absolute Error Between Real and Predicted")

fig.tight_layout()
plt.show()
"""# <-- comment/uncomment this line to switch functionality

