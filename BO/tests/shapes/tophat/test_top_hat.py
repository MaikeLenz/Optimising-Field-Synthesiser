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
#note: the time array must have the same spacing for the synthesiser and for the goal field!
t=np.linspace(0,100,10000)
#we want 50fs, so this is fraction of the whole t array
t_goal=t[:int((30/100)*10000)]
print(len(t_goal))
I_goal_mid=10*np.ones(len(t_goal)-20)
I_goal1=np.append(np.zeros((10)),I_goal_mid)
I_goal=np.append(I_goal1,np.zeros((10)))
print(len(I_goal))
#parameters to be optimised
params=['wavel1','wavel2','wavel3','wavel4','wavel5','wavel6','wavel7','wavel8','wavel9','wavel10','wavel11','wavel12','wavel13','wavel14','wavel15',
'CEP1','CEP2','CEP3','CEP4','CEP5','CEP6','CEP7','CEP8','CEP9','CEP10','CEP11','CEP12','CEP13','CEP14','CEP15',
'fwhm1','fwhm2','fwhm3','fwhm4','fwhm5','fwhm6','fwhm7','fwhm8','fwhm9','fwhm10','fwhm11','fwhm12','fwhm13','fwhm14','fwhm15',
'amp1','amp2','amp3','amp4','amp5','amp6','amp7','amp8','amp9','amp10','amp11','amp12','amp13','amp14','amp15','delay1','delay2','delay3','delay4','delay5','delay6','delay7']
BO(params, Synth, errorCorrectionAdvanced_int, 500,500, t=t,goal_field=I_goal)

#outcome
#{'target': -0.018358194570665277, 'params': {'CEP1': 5.381370484401772, 'CEP10': 3.1564364606076416, 'CEP11': 0.7921526998994857, 'CEP12': 0.6580954908288107, 'CEP13': 0.26504878285603767, 'CEP14': 1.5685449731125327, 'CEP15': 1.3523121865275414, 'CEP2': 2.09344758756572, 'CEP3': 3.1032989563094255, 'CEP4': 3.3055870929240014, 'CEP5': 1.4248060953994217, 'CEP6': 3.71592890235978, 'CEP7': 4.891836026486653, 'CEP8': 4.964278726520479, 'CEP9': 3.027827381809074, 'amp1': 0.3972402698208497, 'amp10': 0.8045311672208532, 'amp11': 0.44257002528698297, 'amp12': 0.41193660115764263, 'amp13': 0.7813994960145325, 'amp14': 0.25817547545861524, 'amp15': 0.4198403338546205, 'amp2': 0.2575749486824803, 'amp3': 0.39055650326922253, 'amp4': 0.6515197536713793, 'amp5': 0.14857309579844574, 'amp6': 0.25299618273665364, 'amp7': 0.5783801391894313, 'amp8': 0.5026507513316698, 'amp9': 0.321265229480028, 'delay1': -0.5865298226012801, 'delay2': -1.8935616779557352, 'delay3': 4.331979670526332, 'delay4': -0.3717022853016907, 'delay5': 2.906482293843961, 'delay6': -3.839193381796213, 'delay7': -2.9647872162333053, 'fwhm1': 65.76307538075741, 'fwhm10': 17.131975334531436, 'fwhm11': 26.917429625314245, 'fwhm12': 8.476431164261985, 'fwhm13': 64.80165835887628, 'fwhm14': 62.459085556798875, 'fwhm15': 40.92264032629208, 'fwhm2': 35.753477951938066, 'fwhm3': 47.45742319487844, 'fwhm4': 44.06829268923814, 'fwhm5': 49.339601034284385, 'fwhm6': 25.16836714224402, 'fwhm7': 25.179425245721788, 'fwhm8': 44.12473116163049, 'fwhm9': 
#36.12237727138468, 'wavel1': 9841.52871574774, 'wavel10': 2491.9003842102293, 'wavel11': 7933.098238904028, 'wavel12': 6517.7663802291445, 'wavel13': 9570.926545784512, 'wavel14': 6003.600907425913, 'wavel15': 7121.60276640164, 'wavel2': 8041.651602955444, 'wavel3': 6194.093225377635, 'wavel4': 7975.997668759559, 'wavel5': 7992.019905780316, 'wavel6': 7269.764625921876, 'wavel7': 4218.590538419461, 'wavel8': 4790.686845908009, 'wavel9': 4761.7722120474145}}