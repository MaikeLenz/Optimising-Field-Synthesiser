import numpy as np
import matplotlib.pyplot as plt
from bayes_opt import BayesianOptimization

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


# Bounded region of parameter space
pbounds = {'x': (-2, 2), 'y': (-2, 2)}

error=100
iterations=0
optimizer = BayesianOptimization(
f=func,
pbounds=pbounds,
verbose=1, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
random_state=1,
)
optimizer.maximize(init_points=90,n_iter=0)

while error>0.01:
    iterations+=1
    optimizer.maximize(init_points=0,n_iter=1)
    print(iterations, optimizer.max)
    error=(optimizer.max["params"]["x"])**2+(optimizer.max["params"]["y"]+1)**2
        
print(iterations, error)
#0 initial points: needed 130 iterations, error 0.00572
#5 initial points: needed 9 iterations, error 0.00522
#10 initial points: needed 172 iterations, 0.000350
