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
y, x = np.meshgrid(np.linspace(-5, 5, 200), np.linspace(-5, 5, 200))
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
iter=100

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
z_min, z_max = -np.abs(z).max(), np.abs(z).max()

fig, ax = plt.subplots()

c = ax.pcolormesh(x, y, z, vmin=z_min, vmax=z_max)
ax.set_title('Sphere')
# set the limits of the plot to the limits of the data
ax.axis([x.min(), x.max(), y.min(), y.max()])
fig.colorbar(c, ax=ax)
markers=range(len(xiter))
#plt.scatter(xinit,yinit,s=10, color="black")
plt.scatter(xiter,yiter,s=10,c=markers,cmap="pink")
plt.scatter(optimizer.max["params"]["x"],optimizer.max["params"]["y"],color="orange", s=15,label="Result")
plt.scatter(0,0,color="red",label="Minimum",s=15)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()