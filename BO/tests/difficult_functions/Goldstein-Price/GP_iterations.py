import numpy as np
import matplotlib.pyplot as plt

def func(x, y):
    """
    returns the negative of the Goldstein-Price function
    """
    return -((1+((x+y+1)**2)*(19-14*x+3*x**2-14*y+6*x*y+3*y**2))*(30+((2*x-3*y)**2)*(18-32*x+12*x**2+48*y-36*x*y+27*y**2)))

# generate 2 2d grids for the x & y bounds
y, x = np.meshgrid(np.linspace(-2, 2, 200), np.linspace(-2, 2, 200))
#z as a function of x and y
z=((1+((x+y+1)**2)*(19-14*x+3*x**2-14*y+6*x*y+3*y**2))*(30+((2*x-3*y)**2)*(18-32*x+12*x**2+48*y-36*x*y+27*y**2)))
#z = (1+(x+y+1)**2*(19-14*x+3*x**2-14*y+6*x*y+3*y**2))*(30+(2*x-3*y)**2*(18-32*x+12*x**2+48*y-36*x*y+27*y**2))  


from bayes_opt import BayesianOptimization

# Bounded region of parameter space
pbounds = {'x': (-2, 2), 'y': (-2, 2)}


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
z_min, z_max = z.min(), np.abs(z).max()

fig, ax = plt.subplots()

c = ax.pcolormesh(x, y, z, vmin=z_min, vmax=z_max)
ax.set_title('Goldstein-Price')
# set the limits of the plot to the limits of the data
ax.axis([x.min(), x.max(), y.min(), y.max()])
fig.colorbar(c, ax=ax)
markers=range(len(xiter))
#plt.scatter(xinit,yinit,s=10, color="black")
plt.scatter(xiter,yiter,c=markers,cmap="pink", marker="+")
plt.scatter(optimizer.max["params"]["x"],optimizer.max["params"]["y"],color="cyan", s=25,label="Result")
plt.scatter(0,-1,color="blue",label="Minimum",s=25)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()