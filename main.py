#import random
#import Player
#from Pack import Pack
from Sim import Sim
from Filter import Filter
import matplotlib.pyplot as plt
import numpy as np

me = Filter()
sim = Sim(18,1,me)


#sim.print_pool()

sim.run_sim()

w,u,b,r,g = me.get_filter()
w1,u1,b1,r1,g1 = sim.get_averages()
t = np.arange(0,len(w),1)

difs = np.empty(len(t))
for i in range(len(t)):
    difs[i] = (w1[i]-w[i]+u1[i]-u[i]+b1[i]-b[i]+r1[i]-r[i]+g1[i]-g[i])
#print(f"len(w) = {len(w)}, len(t) = {len(t)}")

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
g_ax.set_xlabel("Green Belief")
dif_ax.set_xlabel("Difference Between Real and Predicted")

fig.tight_layout()
plt.show()
