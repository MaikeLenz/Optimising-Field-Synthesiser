import numpy as np
import matplotlib.pyplot as plt
from bayes_opt import BayesianOptimization

def func(x, y):
    """
    returns the negative of the Ackley function
    """
    return -(-20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2)))-np.exp(0.5 * (np.cos(2 * np.pi * x)+np.cos(2 * np.pi * y))) + np.e + 20)

# generate 2 2d grids for the x & y bounds
y, x = np.meshgrid(np.linspace(-5, 5, 200), np.linspace(-5, 5, 200))
#z as a function of x and y
z = -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2)))-np.exp(0.5 * (np.cos(2 * np.pi * x)+np.cos(2 * np.pi * y))) + np.e + 20

# Bounded region of parameter space
pbounds = {'x': (-5, 5), 'y': (-5, 5)}

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
    error=optimizer.max["params"]["x"]**2+optimizer.max["params"]["y"]**2
        
print(iterations, error)
#0 initial points:needed 52 iterations, error 7.11e-5
#5 initial points: needed 25 iterations, error 0.00162
#10 initial points: needed 32 iterations, 0.00339