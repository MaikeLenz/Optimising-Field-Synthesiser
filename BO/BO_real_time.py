from bayes_opt import BayesianOptimization

#optimise an external progress, allows manual input during each iteration

optimizer = BayesianOptimization(
    f=None,
    pbounds={'x': (-2, 2), 'y': (-3, 3)},
    verbose=2,
    random_state=1,
)

from bayes_opt import UtilityFunction

utility = UtilityFunction(kind="ucb", kappa=2.5, xi=0.0)

next_point_to_probe = optimizer.suggest(utility)
print("Next point to probe is:", next_point_to_probe)

target =  float(input("What is the target? "))
print("Found the target value to be:", target)

optimizer.register(
    params=next_point_to_probe,
    target=target,
)

for _ in range(10):
    next_point = optimizer.suggest(utility)
    target = input("What is the target? ")
    optimizer.register(params=next_point, target=target)
    
    print(target, next_point)
print(optimizer.max)