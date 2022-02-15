# rastrigin_graph.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm 
from mpl_toolkits.mplot3d import Axes3D 
"""
X = np.linspace(-5.12, 5.12, 100)     
Y = np.linspace(-5.12, 5.12, 100)     
X, Y = np.meshgrid(X, Y) 

Z = (X**2 - 10 * np.cos(2 * np.pi * X)) + \
  (Y**2 - 10 * np.cos(2 * np.pi * Y)) + 20
 
fig = plt.figure() 

plt.colormap(x,y,z)
#3d plot
#ax = fig.gca(projection='3d') 
#ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
#  cmap=cm.nipy_spectral, linewidth=0.08,
#  antialiased=True)    
# plt.savefig('rastrigin_graph.png')

"""

# generate 2 2d grids for the x & y bounds
y, x = np.meshgrid(np.linspace(-5.12, 5.12, 200), np.linspace(-5.12, 5.12, 200))
#z as a function of x and y
z = (x**2 - 10 * np.cos(2 * np.pi * x)) + \
  (y**2 - 10 * np.cos(2 * np.pi * y)) + 20

#now make this the target function
def func(x, y):
    """
    Rastrigin function
    """
    return (x**2 - 10 * np.cos(2 * np.pi * x)) + (y**2 - 10 * np.cos(2 * np.pi * y)) + 20


from bayes_opt import BayesianOptimization

# Bounded region of parameter space
pbounds = {'x': (-5.12, 5.12), 'y': (-5.12, 5.12)}


optimizer = BayesianOptimization(
    f=func,
    pbounds=pbounds,
    verbose=2, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
    random_state=1,
)


optimizer.maximize(
    init_points=100,
    n_iter=0,
)

print(optimizer.max)

#get probed coordinates
xcoords=[]
ycoords=[]
for i, res in enumerate(optimizer.res):
    print("Iteration {}: \n\t{}".format(i, res))
    xcoords.append(res['params']['x'])
    ycoords.append(res['params']['y'])

xcoords=np.array(xcoords)
ycoords=np.array(ycoords)

# x and y are bounds, so z should be the value *inside* those bounds.
# Therefore, remove the last value from the z array.
z = z[:-1, :-1]
z_min, z_max = -np.abs(z).max(), np.abs(z).max()

fig, ax = plt.subplots()

c = ax.pcolormesh(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
ax.set_title('Rastrigin')
# set the limits of the plot to the limits of the data
ax.axis([x.min(), x.max(), y.min(), y.max()])
fig.colorbar(c, ax=ax)
for i in range(len(xcoords)):
    plt.scatter(xcoords[i],ycoords[i], label="iteration %s"%i)
plt.legend()
plt.show()