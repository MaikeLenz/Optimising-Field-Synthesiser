
import numpy as np
from scipy import integrate
import statistics
#this is an updated version which uses integration functions from scipy rather than manual integration which dramatically speeds up the code.

#defines the rms error minimisation functions. 
#errorCorrection_int just works with two given arrays.
#errorCorrectionAdvanced_int normalises them and shifts them in time to align before calculating the errors.

def errorCorrection_int(t, synth_field, goal_field): #both synth_field and goal_field are intensities!
    """
    returns the negative of the rms error between synth_field and goal_field
    without any adjustment in amplitudes or position in time
    """
    diff = np.array([]) #array of the square of differences between intensity and goal function
    if len(synth_field) != len(goal_field):
        print('Error- synth_field is a different length to goal_field')
    for i in range(len(synth_field)):
        diff=np.append(diff,[(synth_field[i] - goal_field[i])**2])
    return - np.sqrt(integrate.simps(diff, t)) #integrates the differences

def errorCorrectionAdvanced_int(t, synth_field, goal_field):
    """
    finds rms error between two functions, first scales them and matches up maxima in time.
    """
    # First scale both functions to amplitude of 1
    #need to check that the norm isn't zero to avoid errors
    if np.linalg.norm(np.array(synth_field)) != 0:
        synth_field=np.array(synth_field)/(np.linalg.norm(np.array(synth_field))) #normalise arrays
    if np.linalg.norm(np.array(goal_field)) != 0:
        goal_field=np.array(goal_field)/(np.linalg.norm(np.array(goal_field)))

    # Next shift the maxima to the same time values- consider only the first maximum for simplicity
    max_indices_synth = np.argwhere(synth_field == np.amax(synth_field)).flatten().tolist()
    max_indices_goal = np.argwhere(goal_field == np.amax(goal_field)).flatten().tolist()
    median_synth = statistics.median(max_indices_synth)
    median_goal = statistics.median(max_indices_goal) 

    offset = int(median_synth - median_goal) #might not be a perfect shift, limited to integer values
    
    if len(synth_field) > len(goal_field):
        #if goal field is shorter, then we only care about that section of the intensity distribution.
        #line up the fields
        #chop off the uninteresting part of the synthesised field here
        #need the point at median_synth to become the index median_goal to line fields up
        if offset >0:
            #crop synth field to the length of the goal field but starting after offset such that maxima align
            synth_field=synth_field[offset:offset+len(goal_field)]
            t=t[:len(goal_field)]
        elif offset<0:
            #have to pad start of synth field to line up with the goal
            synth_field= np.append(np.zeros(abs(offset)),synth_field)
            synth_field=synth_field[:len(goal_field)]
            t=t[:len(goal_field)]



    #determine point that falls below 10% of max which is the limit for being cut off?
    """
    args_below_ten = np.argwhere(synth_field <= 0.1*np.amax(synth_field))#
    args_below_ten_reverse = args_below_ten[::-1] #reverses array
    edge_left = np.argwhere(args_below_ten_reverse < median_synth)
    edge_right = np.argwhere(args_below_ten > median_synth)
    """
    #should we be slicing the synthesised field ?
    """
    if offset > 0: #goal_field on the left of synth_field
        goal_field = goal_field[:len(synth_field)-abs(offset)]
        goal_field=np.append(np.zeros(abs(offset)),goal_field)
    elif offset < 0: #goal_field on the right of synth_field
        goal_field = goal_field[abs(offset):]
        goal_field=np.append(goal_field,np.zeros(abs(offset)))
    """

    return errorCorrection_int(t,synth_field,goal_field) #now carry out rms minimisation with aligned and normalised arrays


def Gauss(x, A, u, o):
    return A*np.exp(-((x-u)**2)/(2*(o**2)))

#testing code 

"""
#%%
# Testing errorCorrection
t = np.arange(0, 50, 0.1)
synth_field = Gauss(t, 1, 25, 5)


# Test function against itself
plt.figure()
plt.plot(t, synth_field, label='original')
plt.legend()
print(errorCorrection(t, synth_field, synth_field)) # Should be zero


# Test against function shifted in time (delayed)
goal_field = Gauss(t+5, 1, 25, 5)
plt.figure()
plt.plot(t, synth_field, label='original')
plt.plot(t, goal_field, label='shifted')
plt.legend()
print(errorCorrection(t, synth_field, goal_field))

# Shift more in time- should be a larger error
goal_field = Gauss(t+10, 1, 25, 5)
plt.figure()
plt.plot(t, synth_field, label='original')
plt.plot(t, goal_field, label='shifted')
plt.legend()
print(errorCorrection(t, synth_field, goal_field))

# Change amplitude and width
goal_field = Gauss(t, 5, 25, 5)
plt.figure()
plt.plot(t, synth_field, label='original')
plt.plot(t, goal_field, label='shifted')
print(errorCorrection(t, synth_field, goal_field))
E3 = Gauss(t, 1, 25, 10)
plt.plot(t, E3, label='broader')
plt.legend()
print(errorCorrection(t, synth_field, E3))
"""
#%%
"""
# Test advanced error correction function
t = np.arange(0, 50, 0.1)
synth_field = Gauss(t, 1, 25, 5)
goal_field = Gauss(t+5, 5, 25, 5)
errorCorrectionAdvanced(t, synth_field, goal_field)
"""
