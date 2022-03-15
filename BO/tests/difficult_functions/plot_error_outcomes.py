import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)
inits=np.array([0,1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100])
iters_booth=np.array([26,26,29,23,78,25,25,78,42,15,21,23,20,3,4,4,3,3,5,21])
iters_ackley=np.array([52,52,37,40,10,25,28,41,32,9,32,15,22,8,7,9,6,10,7,8])
iters_sphere=np.array([14,14,15,15,16,15,14,11,12,13,12,8,7,5,4,4,4,4,1,1])
iters_matyas=np.array([34,34,34,36,47,29,54,63,30,32,47,17,15,10,5,4,11,39,2,2])

def func(x,a,b,c):
    return a*np.exp(-b*x)+c

from scipy.optimize import curve_fit

popt_ackley,_=curve_fit(func,inits,iters_ackley)
popt_booth,_=curve_fit(func,inits,iters_booth)
popt_sphere,_=curve_fit(func,inits,iters_sphere)
popt_matyas,_=curve_fit(func,inits,iters_matyas)

def sum(x,y):
    s=[]
    for i in range(len(x)):
        i.append(i+y[i])
    return np.array(s)

plt.plot(inits,iters_booth,label="Booth function",marker="+",ls="None")
plt.plot(inits, iters_ackley, label="Ackley function",marker="+",ls="None")
plt.plot(inits, iters_sphere, label="Sphere function",marker="+",ls="None")
plt.plot(inits, iters_matyas, label="Matyas function",marker="+",ls="None")

plt.plot(inits,func(inits,*popt_ackley),color=plt.cm.Set2(1))
plt.plot(inits,func(inits,*popt_booth),color=plt.cm.Set2(0))
plt.plot(inits,func(inits,*popt_sphere),color=plt.cm.Set2(2))
plt.plot(inits,func(inits,*popt_matyas),color=plt.cm.Set2(3))

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title("Penetrating within 0.1 of global optima of difficult functions", fontsize=20)
plt.xlabel("Random Initial Points", fontsize=16)
plt.ylabel("Number of iterations required",fontsize=16)

plt.legend(fontsize=14)

plt.show()