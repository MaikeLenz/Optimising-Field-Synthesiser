import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm 
from bayes_opt import BayesianOptimization

def func(x, y):
    """
    returns the negative of the sphere function
    """
    return -(x**2+y**2)

# generate 2 2d grids for the x & y bounds
y, x = np.meshgrid(np.linspace(-0.12, 0.12, 200), np.linspace(-0.12, 0.12, 200))
#z as a function of x and y
z = x**2+y**2

pbounds = {'x': (-5, 5), 'y': (-5, 5)}


optimizer = BayesianOptimization(
    f=func,
    pbounds=pbounds,
    verbose=2, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
    random_state=1,
)

init=100
iter=10

optimizer.maximize(
    init_points=init,
    n_iter=iter,
)

print(optimizer.max)

#get probed coordinates
xcoords=[]
ycoords=[]
for i, res in enumerate(optimizer.res):
    #print("Iteration {}: \n\t{}".format(i, res))
    xcoords.append(res['params']['x'])
    ycoords.append(res['params']['y'])

xcoords=np.array(xcoords)
xinit=xcoords[:init]
xiter=xcoords[init:]
ycoords=np.array(ycoords)
yinit=ycoords[:init]
yiter=ycoords[init:]

# x and y are bounds, so z should be the value *inside* those bounds.
# Therefore, remove the last value from the z array.
z = z[:-1, :-1]
z_min, z_max = z.min(), z.max()

fig, ax = plt.subplots()

c = ax.pcolormesh(x, y, z, vmin=z_min, vmax=z_max, cmap=plt.get_cmap('gray'))
ax.set_title('Sphere', fontsize=20)
# set the limits of the plot to the limits of the data
ax.axis([x.min(), x.max(), y.min(), y.max()])

#ax.axis([-0.1,0.1,-0.1,0.1])
cb=fig.colorbar(c, ax=ax)
cb.set_label("Value", labelpad=1, size=14)
cb.ax.tick_params(labelsize=14)

#markers=range(len(xiter))
#plt.scatter(xinit,yinit,s=10, color="black")
#plt.scatter(xiter,yiter,s=10,c=markers,cmap="pink")
plt.scatter(xiter,yiter,c="white", marker="o")

plt.plot(xiter,yiter,marker="None",color="white")
 
plt.scatter(optimizer.max["params"]["x"],optimizer.max["params"]["y"],color="tab:blue", s=100,label="Result")
plt.scatter(xiter[0],yiter[0],color="green", s=100,label="Start")
plt.scatter(0,0,color="red",label="Minimum",s=100)
plt.xlabel("x",fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel("y",fontsize=16)
plt.legend(fontsize=14)
plt.show()