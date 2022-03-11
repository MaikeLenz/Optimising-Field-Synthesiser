import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)
def func(x, y):
    """
    returns the negative of the Bukin function
    """
    return -(100*np.sqrt(np.abs(y-0.01*x**2))+0.01*np.abs(x+10))

# generate 2 2d grids for the x & y bounds
y, x = np.meshgrid(np.linspace(-3, 3, 200), np.linspace(-15, -5, 200))
#z as a function of x and y
z=100*np.sqrt(np.abs(y-0.01*x**2))+0.01*np.abs(x+10)


from bayes_opt import BayesianOptimization

# Bounded region of parameter space
pbounds = {'x': (-15, -5), 'y': (-3, 3)}


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
z_min, z_max = z.min(), np.abs(z).max()

fig, ax = plt.subplots()

c = ax.pcolormesh(x, y, z, vmin=z_min, vmax=z_max)
ax.set_title('Bukin')
# set the limits of the plot to the limits of the data
ax.axis([x.min(), x.max(), y.min(), y.max()])
fig.colorbar(c, ax=ax)
markers=range(len(xiter))
#plt.scatter(xinit,yinit,s=10, color="black")
#plt.scatter(xiter,yiter,c=markers, marker="+")
plt.scatter(xiter,yiter,c="black", marker="o")

plt.plot(xiter,yiter,marker="None",color="black")
plt.scatter(optimizer.max["params"]["x"],optimizer.max["params"]["y"],color="cyan", s=25,label="Result")
plt.scatter(-10,1,color="blue",label="Minimum",s=25)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()