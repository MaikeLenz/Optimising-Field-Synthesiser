import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16

df = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\Optimise_Lab\\saved_iterations\\Ne_Exp_Input.csv")
iteration = df.iloc[:,0]
target_width = df.iloc[:,1] # \m
energy = df.iloc[:,2] # J
pressure = df.iloc[:,3] # bar
grating_pos = df.iloc[:,4] # m

plt.plot(iteration[:100], target_width[:100], 'x', label='Initial Points')
plt.plot(iteration[100:], target_width[100:], 'x', label='Iterations')
plt.legend()
plt.xlabel('Number of Evaluations')
plt.ylabel('RMS Width, \m')
plt.show()