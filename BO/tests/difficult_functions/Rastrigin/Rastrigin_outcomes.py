# rastrigin_graph.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm 
from mpl_toolkits.mplot3d import Axes3D 

# generate 2 2d grids for the x & y bounds
y, x = np.meshgrid(np.linspace(-5.12, 5.12, 200), np.linspace(-5.12, 5.12, 200))
#z as a function of x and y
z = (x**2 - 10 * np.cos(2 * np.pi * x)) + \
  (y**2 - 10 * np.cos(2 * np.pi * y)) + 20

#now make this the target function
def func(x, y):
    """
    negative of the Rastrigin function
    BO maximises but the Rastrigin function has a global minimum
    """
    return - ((x**2 - 10 * np.cos(2 * np.pi * x)) + (y**2 - 10 * np.cos(2 * np.pi * y)) + 20)


from bayes_opt import BayesianOptimization

# Bounded region of parameter space
pbounds = {'x': (-5.12, 5.12), 'y': (-5.12, 5.12)}

inits=np.arange(10,130,30)
iters=np.arange(10,130,30)

#inits=np.array([1,2])
#iters=np.array([1,2])
results={}
for i in inits:
    for j in iters:
        optimizer = BayesianOptimization(
        f=func,
        pbounds=pbounds,
        verbose=1, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
        random_state=1,
        )

        optimizer.maximize(
            init_points=i,
            n_iter=j,
        )

        print(optimizer.max)
        
        results["%s,%s"%(i,j)]=[optimizer.max["params"]["x"],optimizer.max["params"]["y"]]

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

i=0
colours = cm.pink(np.linspace(0, 1, len(results)))
for key, value in results.items():
    plt.scatter(value[0],value[1],label=key,s=15,c=colours[i])
    i+=1
plt.scatter(0,0,color="red",label="Minimum",s=20)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()