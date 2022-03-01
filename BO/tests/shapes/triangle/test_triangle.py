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
def triang(x,a,b):
    return a*x+b
#note: the time array must have the same spacing for the synthesiser and for the goal field!
t=np.linspace(0,100,10000)
#we want 50fs, so this is fraction of the whole t array
t_goal=t[:int((30/100)*10000)]
print(len(t_goal))
t_crop=t_goal[10:len(t_goal)-10]
I_goal_mid=np.append(triang(t_crop[:int(len(t_crop)/2)],10/15,0),triang(t_crop[int(len(t_crop)/2):],-10/15,20))
I_goal1=np.append(np.zeros((10)),I_goal_mid)
I_goal=np.append(I_goal1,np.zeros((10)))
print(len(I_goal))
#parameters to be optimised
params=['wavel1','wavel2','wavel3','wavel4','wavel5','wavel6','wavel7','wavel8','wavel9','wavel10','wavel11','wavel12','wavel13','wavel14','wavel15',
'CEP1','CEP2','CEP3','CEP4','CEP5','CEP6','CEP7','CEP8','CEP9','CEP10','CEP11','CEP12','CEP13','CEP14','CEP15',
'fwhm1','fwhm2','fwhm3','fwhm4','fwhm5','fwhm6','fwhm7','fwhm8','fwhm9','fwhm10','fwhm11','fwhm12','fwhm13','fwhm14','fwhm15',
'amp1','amp2','amp3','amp4','amp5','amp6','amp7','amp8','amp9','amp10','amp11','amp12','amp13','amp14','amp15','delay1','delay2','delay3','delay4','delay5','delay6','delay7']
BO(params, Synth, errorCorrectionAdvanced_int, 100,100, t=t,goal_field=I_goal)

#outcome
#{'target': -0.008067832111449307, 'params': {'CEP1': 4.309717263253735, 'CEP10': 5.127882319707595, 'CEP11': 0.9691566245011973, 'CEP12': 1.1636060309777836, 'CEP13': 3.4092235561488478, 'CEP14': 0.38577663826110825, 'CEP15': 3.380721377040232, 'CEP2': 2.111131421105479, 'CEP3': 2.038606662642698, 'CEP4': 1.444210180781528, 'CEP5': 0.029447653433432266, 'CEP6': 4.317009152904894, 'CEP7': 4.729863728167617, 'CEP8': 2.125497388901069, 'CEP9': 2.9518631933138377, 'amp1': 0.8176440465827077, 'amp10': 0.6827209650597291, 'amp11': 0.12068035460433658, 'amp12': 0.35557523690373727, 'amp13': 0.9589553486637115, 'amp14': 0.8948391898618238, 'amp15': 0.39269615597103613, 'amp2': 0.9195705003642172, 'amp3': 0.5312575736802193, 'amp4': 0.2818618487079528, 'amp5': 0.3443044673065695, 'amp6': 0.3168837247525049, 'amp7': 0.15001791068326364, 'amp8': 0.493422500118718, 'amp9': 0.9141245987713534, 'delay1': 0.25757464179263145, 'delay2': 0.4545647290553143, 'delay3': -2.7300038983446386, 'delay4': -4.535991702588409, 'delay5': -3.7419197720212347, 'delay6': -2.8487430718835602, 'delay7': 3.7339341540935607, 'fwhm1': 69.24135963610352, 'fwhm10': 6.154806157115791, 'fwhm11': 33.81514709060558, 'fwhm12': 28.997823901055842, 'fwhm13': 39.870131628284454, 'fwhm14': 45.07398321154031, 'fwhm15': 30.73998447805382, 'fwhm2': 16.951164172184043, 'fwhm3': 43.04282597833027, 'fwhm4': 7.164290026370037, 'fwhm5': 63.10854822606295, 'fwhm6': 46.88670183084754, 'fwhm7': 11.14537717662153, 'fwhm8': 40.83937406973239, 'fwhm9': 13.383330874362034, 'wavel1': 1540.6800653650098, 'wavel10': 2949.269455284485, 'wavel11': 7723.919695087071, 'wavel12': 7102.921080408408, 'wavel13': 5764.980490569512, 'wavel14': 2850.1755404016785, 'wavel15': 5371.540163421709, 'wavel2': 9325.609538641682, 'wavel3': 2179.0643495866307, 'wavel4': 7448.391108639098, 'wavel5': 8772.955808800374, 'wavel6': 6826.779600548402, 'wavel7': 2355.478419096244, 'wavel8': 1639.993565168091, 'wavel9': 5344.316717177792}}