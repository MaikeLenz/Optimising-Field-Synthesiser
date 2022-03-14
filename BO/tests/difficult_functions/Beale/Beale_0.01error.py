import numpy as np
import matplotlib.pyplot as plt
from bayes_opt import BayesianOptimization

def func(x, y):
    """
    negative of the Rastrigin function
    BO maximises but the Rastrigin function has a global minimum
    """
    return - ((1.5-x+x*y)**2+(2.25-x+x*y**2)**2+(2.625-x+x*y**3)**2)


# Bounded region of parameter space
pbounds = {'x': (-4.5, 4.5), 'y': (-4.5, 4.5)}

error=100
iterations=0
optimizer = BayesianOptimization(
f=func,
pbounds=pbounds,
verbose=1, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
random_state=1,
)
optimizer.maximize(init_points=100,n_iter=0)

while error>0.01:
    iterations+=1
    optimizer.maximize(init_points=0,n_iter=1)
    print(iterations, optimizer.max)
    error=(optimizer.max["params"]["x"]-3)**2+(optimizer.max["params"]["y"]-0.5)**2
        
print(iterations, error)