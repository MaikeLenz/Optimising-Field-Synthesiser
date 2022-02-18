import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm 
from adjustText import adjust_text

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

inits=np.arange(10,130,30)
iters=np.arange(10,130,30)

labels=[]

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
        labels.append(str(i)+","+str(j))

# x and y are bounds, so z should be the value *inside* those bounds.
# Therefore, remove the last value from the z array.
z = z[:-1, :-1]
z_min, z_max = z.min(), np.abs(z).max()

fig, ax = plt.subplots()

#c = ax.pcolormesh(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
c = ax.pcolormesh(x, y, z, vmin=z_min, vmax=z_max)
ax.set_title('Goldstein-Price')
# set the limits of the plot to the limits of the data
ax.axis([x.min(), x.max(), y.min(), y.max()])
fig.colorbar(c, ax=ax)

i=0
X=np.array([])
Y=np.array([])
colours = cm.pink(np.linspace(0, 1, len(results)))
for key, value in results.items():
    #plt.scatter(value[0],value[1],label=key,s=15,c=colours[i])
    plt.scatter(value[0],value[1],marker="x",c=colours[i])
    X=np.append(X,value[0])
    Y=np.append(Y,value[1])
    i+=1

texts = []
for i, txt in enumerate(labels):
    texts.append(plt.annotate(txt, xy=(X[i], Y[i]), xytext=(X[i],Y[i]+.3)))
    
adjust_text(texts)
"""
for i,txt in enumerate(labels):
    plt.annotate(txt,(X[i],Y[i]))
"""
plt.scatter(0,-1,color="cyan",label="Minimum",s=25)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()