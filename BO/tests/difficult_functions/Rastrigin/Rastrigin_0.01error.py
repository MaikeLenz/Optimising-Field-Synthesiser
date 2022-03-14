import numpy as np
import matplotlib.pyplot as plt
from bayes_opt import BayesianOptimization

def func(x, y):
    """
    negative of the Rastrigin function
    BO maximises but the Rastrigin function has a global minimum
    """
    return - ((x**2 - 10 * np.cos(2 * np.pi * x)) + (y**2 - 10 * np.cos(2 * np.pi * y)) + 20)



# Bounded region of parameter space
pbounds = {'x': (-5.12, 5.12), 'y': (-5.12, 5.12)}

error=100
iterations=0
optimizer = BayesianOptimization(
f=func,
pbounds=pbounds,
verbose=1, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
random_state=1,
)
optimizer.maximize(init_points=70,n_iter=0)

while error>0.01:
    iterations+=1
    optimizer.maximize(init_points=0,n_iter=1)
    print(iterations, optimizer.max)
    error=(optimizer.max["params"]["x"])**2+(optimizer.max["params"]["y"])**2
        
print(iterations, error)
#0 initial points: 9 iterations, 0.00843
#5 initial points: 203 iterations, error 0.00232
#10 initial points: killed at 370 iterations