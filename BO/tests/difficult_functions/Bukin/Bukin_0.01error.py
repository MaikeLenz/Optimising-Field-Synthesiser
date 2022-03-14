import numpy as np
import matplotlib.pyplot as plt
from bayes_opt import BayesianOptimization

def func(x, y):
    """
    returns the negative of the Bukin function
    """
    return -(100*np.sqrt(np.abs(y-0.01*x**2))+0.01*np.abs(x+10))

# generate 2 2d grids for the x & y bounds
y, x = np.meshgrid(np.linspace(-3, 3, 200), np.linspace(-15, -5, 200))
#z as a function of x and y
z=100*np.sqrt(np.abs(y-0.01*x**2))+0.01*np.abs(x+10)

# Bounded region of parameter space
pbounds = {'x': (-15, -5), 'y': (-3, 3)}

error=100
iterations=0
optimizer = BayesianOptimization(
f=func,
pbounds=pbounds,
verbose=1, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
random_state=1,
)
optimizer.maximize(init_points=5,n_iter=0)

while error>0.01:
    iterations+=1
    optimizer.maximize(init_points=0,n_iter=1)
    print(iterations, optimizer.max)
    error=(optimizer.max["params"]["x"]+10)**2+(optimizer.max["params"]["y"]-1)**2
        
print(iterations, error)
#0 initial points: killed at 500 iterations
#5 initial points: killed at 500 iterations