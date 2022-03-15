import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16

df_init = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\Optimise_Lab\\saved_optimum\\Optimal_Params_init.csv")
iteration = df_init.iloc[:,0]
target_width = df_init.iloc[:,1] # \m
energy = df_init.iloc[:,2] # J
pressure = df_init.iloc[:,3] # bar
grating_pos = df_init.iloc[:,4] # m

plt.plot(iteration, target_width, 'x')
plt.xlabel('Evaluation Number')
plt.ylabel('RMS Width, \m')
plt.title('Initial Random Search')

best_init = max(target_width)
mean_init = np.mean(target_width)
print('Best initial random point = {} \m'.format(best_init))
print('Mean initial random point = {} \m'.format(mean_init))

df_iter = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\Optimise_Lab\\saved_optimum\\Optimal_Params_iters.csv")
iteration = df_iter.iloc[:,0]
target_width = df_iter.iloc[:,1] # \m
energy = df_iter.iloc[:,2] # J
pressure = df_iter.iloc[:,3] # bar
grating_pos = df_iter.iloc[:,4] # m

plt.figure()
plt.plot(iteration, target_width, 'x')
plt.xlabel('Number of Iterations')
plt.ylabel('RMS Width, \m')
plt.title('Optimum Found After a Given Number of Iterations')

best_iter = max(target_width)
print('Optimum after iterations = {} \m'.format(best_iter))
print('Increase from mean by factor {} %'.format((1 - best_iter/mean_init)*100))

plt.show()