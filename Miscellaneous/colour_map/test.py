import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)

x=np.linspace(0,100,1000)
y1=x
y2=2*x
y3=3*x
y4=4*x

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)

plt.show()