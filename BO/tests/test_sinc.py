#imports
import numpy as np
from bayes_opt import BayesianOptimization
import matplotlib.pyplot as plt

#now import the code form the other files
import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
from subtargetfunctions import *
from bossfunction import *
from field_synth_class import *
#from ErrorCorrectionFunction import * #out of date functions
from ErrorCorrectionFunction_integrate import *

"""
test if the bossfunction works to mimic rms error and reproduce a linear ramp
"""
#create fields
Field1=Wavepacket(t0=50.0, wavel=400.0, fwhm=40.0, amp=1.0, CEP=0.0)
Field2=Wavepacket(t0=50.0, wavel=700.0, fwhm=40.0, amp=1.0, CEP=0.0)
Field3=Wavepacket(t0=50.0, wavel=1000.0, fwhm=40.0, amp=1.0, CEP=0.0)
Field4=Wavepacket(t0=50.0, wavel=2000.0, fwhm=40.0, amp=1.0, CEP=0.0)
Field5=Wavepacket(t0=50.0, wavel=1500.0, fwhm=40.0, amp=1.0, CEP=0.0)
Field6=Wavepacket(t0=50.0, wavel=700.0, fwhm=40.0, amp=1.0, CEP=0.0)
Field7=Wavepacket(t0=50.0, wavel=1000.0, fwhm=40.0, amp=1.0, CEP=0.0)
Field8=Wavepacket(t0=50.0, wavel=2000.0, fwhm=40.0, amp=1.0, CEP=0.0)
Field9=Wavepacket(t0=50.0, wavel=1500.0, fwhm=40.0, amp=1.0, CEP=0.0)
Field10=Wavepacket(t0=50.0, wavel=700.0, fwhm=40.0, amp=1.0, CEP=0.0)
Field11=Wavepacket(t0=50.0, wavel=1000.0, fwhm=40.0, amp=1.0, CEP=0.0)
Field12=Wavepacket(t0=50.0, wavel=2000.0, fwhm=40.0, amp=1.0, CEP=0.0)
Field13=Wavepacket(t0=50.0, wavel=1500.0, fwhm=40.0, amp=1.0, CEP=0.0)
Field14=Wavepacket(t0=50.0, wavel=4000.0, fwhm=40.0, amp=1.0, CEP=0.0)
Field15=Wavepacket(t0=50.0, wavel=1500.0, fwhm=40.0, amp=1.0, CEP=0.0)
#initialise pulse list and tuple of relative delays (from 1st pulse)
pulses=[Field1,Field2, Field3, Field4, Field5,Field6,Field7,Field8,Field9,Field10,Field11,Field12,Field13,Field14,Field15]
delays=(0,0,0,0,0,0,0,0,0,0,0,0,0,0)
#pass to synthesiser
Synth=Synthesiser(pulses,delays)

#define goal field
def sinc(x):
    return 10*np.abs(np.sin((x-25)/2)/((x-25)/2))
#note: the time array must have the same spacing for the synthesiser and for the goal field!
t=np.linspace(0,100,10000)
#we want 50fs, so this is fraction of the whole t array
t_goal=t[1:int((50/100)*10000)+1]#exclude t=0 to avoid complications

I_goal1=np.append(sinc(-t_goal[:int(len(t_goal)/2)]),np.array([10]))

I_goal=np.append(I_goal1,sinc(t_goal[:int(len(t_goal)/2)]))


print(len(t_goal))
I_goal=sinc(t_goal)
print(len(I_goal))
#parameters to be optimised
params=['wavel1','wavel2','wavel3','wavel4','wavel5','wavel6','wavel7','wavel8','wavel9','wavel10','wavel11','wavel12','wavel13','wavel14','wavel15',
'CEP1','CEP2','CEP3','CEP4','CEP5','CEP6','CEP7','CEP8','CEP9','CEP10','CEP11','CEP12','CEP13','CEP14','CEP15',
'fwhm1','fwhm2','fwhm3','fwhm4','fwhm5','fwhm6','fwhm7','fwhm8','fwhm9','fwhm10','fwhm11','fwhm12','fwhm13','fwhm14','fwhm15',
'amp1','amp2','amp3','amp4','amp5','amp6','amp7','amp8','amp9','amp10','amp11','amp12','amp13','amp14','amp15','delay1','delay2','delay3','delay4','delay5','delay6','delay7']
BO(params, Synth, errorCorrectionAdvanced_int, 100,100 , t=t,goal_field=I_goal)

#outcome
#{'target': -0.02149633086765395, 'params': {'CEP1': 0.9750280654096632, 'CEP10': 2.7021668914071237, 'CEP11': 3.2883330000865207, 'CEP12': 1.953816814188065, 'CEP13': 3.592076725696204, 'CEP14': 2.6830576000998785, 'CEP15': 4.817658508960201, 'CEP2': 5.5568992529610055, 'CEP3': 0.05550595511046051, 'CEP4': 1.2764530780400831, 'CEP5': 3.83064437251445, 'CEP6': 3.3142401589371753, 'CEP7': 3.0206436803547128, 'CEP8': 2.7948243517688987, 'CEP9': 1.7874531109753014, 'amp1': 0.8903467655292193, 'amp10': 0.8708373255726951, 'amp11': 0.4391625600722173, 'amp12': 0.5826685361685234, 'amp13': 0.28776642456697454, 'amp14': 0.8298688706171222, 'amp15': 0.6388966336329178, 'amp2': 0.22504989571721698, 'amp3': 0.9799759464925312, 'amp4': 0.694556052117983, 'amp5': 0.39732798272896097, 'amp6': 0.8997844860470193, 'amp7': 0.7205058804680483, 'amp8': 0.3091184950746757, 'amp9': 0.48119212376702547, 'delay1': 0.34430645292789386, 'delay2': -3.550890888775667, 'delay3': 4.2310331434651545, 'delay4': 2.2519228504445348, 'delay5': 0.23316454181877422, 'delay6': 2.5429376574818683, 'delay7': -1.5800494055007084, 'fwhm1': 6.154660386079486, 'fwhm10': 33.61504428545658, 'fwhm11': 20.301885698034724, 'fwhm12': 33.497284484764, 'fwhm13': 68.50457740743704, 'fwhm14': 36.57780904477594, 'fwhm15': 66.67532857123916, 'fwhm2': 57.702159633417416, 'fwhm3': 25.187691609367537, 'fwhm4': 56.10343964162957, 'fwhm5': 30.914723719827315, 'fwhm6': 22.336964810743833, 'fwhm7': 65.20687051083539, 'fwhm8': 41.059431964004816, 'fwhm9': 42.23245826725119, 'wavel1': 5892.368566259428, 'wavel10': 583.0375619908509, 'wavel11': 1263.181132815529, 'wavel12': 4770.184014174439, 'wavel13': 8273.580211706145, 'wavel14': 5200.744876259893, 'wavel15': 7772.77985839918, 'wavel2': 8279.877277506926, 'wavel3': 1407.6010014761057, 'wavel4': 3081.2069870067166, 'wavel5': 8836.00847501474, 'wavel6': 3502.1920112136327, 'wavel7': 1606.7615204312076, 'wavel8': 5713.636238239853, 'wavel9': 656.239118697058}}