import numpy as np

# booth function min is f(1,3)=0
#bukin min f(-10,1)=0
# ackley min f(0,0)=0

def booth_function(x, y):
    return - (x+2*y-7)**2 - (2*x+y-5)**2

def bukin_function(x, y):
    return -100*np.sqrt(abs(y-0.01*x**2))-0.01*abs(x+10)

def ackley_function(x,y):
    return 20*np.exp(-0.2*np.sqrt(0.5*(x**2+y**2)))+np.exp(0.5*np.cos(2*np.pi*x)+np.cos(2*np.pi*y))- np.exp(1) - 20
from bayes_opt import BayesianOptimization

# Bounded region of parameter space
pbounds_booth = {'x': (-10, 10), 'y': (-10, 10)}
pbounds_bukin = {'x': (-15,-5), 'y': (-3,3)}
pbounds_ackley = {'x': (-5,5), 'y': (-5,5)}

optimizer = BayesianOptimization(
    f=ackley_function,
    pbounds=pbounds_ackley,
    verbose=1, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
    random_state=1,
)


optimizer.maximize(
    init_points=100,
    n_iter= 100,
)


print(optimizer.max)