import numpy as np
from bayes_opt import BayesianOptimization
import matplotlib.pyplot as plt
import statistics
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)

import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
from subtargetfunctions import *
from field_synth_class import *
#from ErrorCorrectionFunction import *
from ErrorCorrectionFunction_integrate import *

#this function carries out BO for N fields. First, it defines the relevant target function before varying the input parameters.

def BO_noplot(params, Synth, function, init_points=50, n_iter=50, goal_field=None, t=np.linspace(-20,100,20000), window=None):     
    """
    performs BO with params as specified as strings in params input (params is list of strings) on the synthesiser Synth.
    init_points: number of initial BO points
    n_iter: number of iterations
    plots output total and individual fields.
    """ 
    params_dict = Synth.create_dict() #returns synthesiser parameters as dictionary
    args_BO = {} #this dictionary will contain only the parameters we want to vary here
    for i in params:
        if i in params_dict:
            args_BO[i]=params_dict[i] #append parameters to be varied to dictionary
        else:
            print('Error! Invalid parameter to vary') #this means that the string entered in params is not one of the recognised options
     #time frame to look at, in fs

    def target_func(**args):
        """
        this is the target function of the optimiser. It is created as a nested function to take only the desired variables as inputs.
        It will consist of one of the sub-target functions in the subtarget function file or one of the rms error functions in ErrorCorrection_integrate.
        """
        E=np.array([])
        I=np.array([])
        # Update the synthesiser's dictionary with new parameters
        for i in range(len(params)):
            params_dict[params[i]] = args[params[i]]
               
        # Now pass dictionary into array full of all the parameters
        # need the parameters in the right order to update the synthesiser
        organised_params = np.zeros((Synth.no_of_channels(),5))
        for key, value in params_dict.items():
            for i in range(Synth.no_of_channels()):
                #print("i is",i)
                if str(i+1) in key:
                    #iterate through parameters and insert into organised params array
                    if 'wavel' in key:
                        organised_params[i][0] = value
                    elif 'fwhm' in key:
                        organised_params[i][1] = value
                    elif 'amp' in key:
                        organised_params[i][2] = value
                    elif 'CEP' in key:
                        organised_params[i][3] = value
                    elif 'delay' in key:
                        organised_params[i][4] = value
        # Now update synthesiser- parameters should be in the right order now
        for i in range(len(organised_params)):
            Synth.Update(i+1 , *organised_params[i]) #passes the parameters to the synthesiser to updatethe channels
        for i in t: 
            #create array of total E field values over range t
            E_i=Synth.E_field_value(i)

            E=np.append(E,[E_i.real])
            I=np.append(I,[np.abs(E_i)**2])
        
        if window!=None:
            #if a window of interest is defined, only care about that section
            max_index = statistics.median(np.argwhere(abs(E) == np.amax(np.absolute(E))).flatten().tolist()) #finds index of middle maximum
            E=E[int(max_index-0.5*window):int(max_index+0.5*window)] #window of defined width with the maximum field in the centre
            #also slice time array accordingly here!
            t1=t[:len(E)]
        else:
            t1=t

        if function==errorCorrectionAdvanced_int or function==errorCorrection_int:
            #to minimise rms errors, the sub-target function contains another argument, the goal intensity field
            return function(t1,I,goal_field)    
        else: 
            #perhaps already pass the array of intensities in here?
            return function(t1,E,I) #pass t E and I to sub-target function

    # Make pbounds dictionary
    pbounds = {}
    for i in params:
        #assume standard bounds, same for each channel
        if 'wavel' in i:
            pbounds[i] = (400,2000)
            #pbounds[i] = (1100,2100)
            #pbounds[i]=(400,10000)
        if 'fwhm' in i:
            pbounds[i] = (5,70)
        if 'GDD' in i:
            pbounds[i] = (-50,0,50)
            #technically need to find GDD bounds here that make sense for our pulse
        if 'amp' in i:
            pbounds[i] = (0.1,1)
        if 'CEP' in i:
            pbounds[i] = (0, 2*np.pi)
        if 'delay' in i:
            pbounds[i] = (-5,5)
    print(pbounds)

    optimizer = BayesianOptimization(
        #now create BO with the defined target function
        f=target_func,
        pbounds=pbounds,
        verbose=1, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
        random_state=1,
        )

    optimizer.maximize(
        #maximises the target function output. In the case of the rms error functions, this is a minimisation because the errors are multiuplied by -1
        init_points=init_points,
        n_iter=n_iter,
        kappa=10
        )

    print(optimizer.max) #final parameters
    return optimizer.max,optimizer.res