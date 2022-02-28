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
def dip(x,a):
    return a*(x-15)**2
#note: the time array must have the same spacing for the synthesiser and for the goal field!
t=np.linspace(0,100,10000)
#we want 50fs, so this is fraction of the whole t array
t_goal=t[:int((30/100)*10000)]
print(len(t_goal))
I_goal_mid=dip(t_goal[10:len(t_goal)-10],10/15**2)
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
#{'target': -0.023362542107608592, 'params': {'CEP1': 2.625309433445063, 'CEP10': 1.9727166597748305, 'CEP11': 1.4057751313304347, 'CEP12': 3.583063209921351, 'CEP13': 4.900404403751832, 'CEP14': 4.833658580359074, 'CEP15': 4.3584645468565215, 'CEP2': 3.613645235450449, 'CEP3': 5.69686570086343, 'CEP4': 0.598524070290253, 'CEP5': 0.22219950458113022, 'CEP6': 1.9682770896892372, 
#'CEP7': 3.458127522657777, 'CEP8': 4.338870618456869, 'CEP9': 1.7378291802103465, 'amp1': 0.34478712213395, 'amp10': 0.17740117753463458, 'amp11': 0.41101217334614526, 'amp12': 0.20334829177460828, 'amp13': 0.43423141137042076, 'amp14': 0.6320120877366732, 'amp15': 0.8544315630630421, 'amp2': 0.2838887010744312, 'amp3': 0.3611545300021426, 'amp4': 0.5700675602848011, 'amp5': 0.44659875389062176, 'amp6': 0.1532458987643105, 'amp7': 0.7882336926178447, 'amp8': 0.2644805138908337, 'amp9': 0.24771932961232246, 'delay1': 1.7578315466284504, 'delay2': 3.316001118425609, 'delay3': 0.954872092993309, 'delay4': -4.097571920030761, 'delay5': 0.2123354386888785, 'delay6': -1.7161504851393774, 'delay7': 0.9614000899002395, 'fwhm1': 37.124449264840386, 'fwhm10': 
#45.91402855672155, 'fwhm11': 66.11300505155128, 'fwhm12': 19.74941674697964, 'fwhm13': 59.04288598590865, 'fwhm14': 12.930671469385357, 'fwhm15': 66.33121894278808, 'fwhm2': 61.022685056478444, 'fwhm3': 36.415658595976865, 'fwhm4': 35.31327193121892, 'fwhm5': 14.089954835523178, 'fwhm6': 68.24741410362296, 'fwhm7': 11.003820198418424, 'fwhm8': 25.772436835820557, 'fwhm9': 53.33483272961694, 'wavel1': 4121.6931336348225, 'wavel10': 7772.869630222547, 'wavel11': 2661.836613483949, 'wavel12': 8984.972025403418, 'wavel13': 5781.91656966899, 'wavel14': 2196.723359051032, 'wavel15': 9605.186594442031, 'wavel2': 2634.2763453673397, 'wavel3': 6696.473707459645, 'wavel4': 5800.258629023902, 'wavel5': 2983.169184101931, 'wavel6': 4260.523863696304, 'wavel7': 3243.4970976189747, 'wavel8': 2526.799197406208, 'wavel9': 1070.16855449292}}


#outcome with edges of goal function padded with zeroes:
#{'target': -0.03582428027649063, 'params': {'CEP1': 2.11640761244306, 'CEP10': 4.092949281000814, 'CEP11': 1.862129349867513, 'CEP12': 0.4082697904896521, 'CEP13': 3.289275880393446, 'CEP14': 0.8657685613622936, 'CEP15': 0.3000592924507162, 'CEP2': 2.4492911347754576, 'CEP3': 2.5782707337821185, 'CEP4': 2.372240557496419, 'CEP5': 5.768747298001759, 'CEP6': 2.934085494600379, 'CEP7': 3.122431849443377, 'CEP8': 3.3357977114821034, 'CEP9': 3.781018486733805, 'amp1': 0.8975241993042834, 'amp10': 0.6181382532983932, 'amp11': 0.4817137008845698, 'amp12': 0.48897320622282026, 'amp13': 0.8694357126712869, 'amp14': 0.4788338902202486, 'amp15': 0.9786193098928949, 'amp2': 0.4559367470603053, 'amp3': 0.8815357039867111, 'amp4': 0.36101404912998813, 'amp5': 0.2628312890152614, 'amp6': 0.6282627437699766, 'amp7': 0.3547645315497894, 'amp8': 0.8897996934364467, 'amp9': 0.5312050247995462, 'delay1': 0.41679925003094986, 'delay2': -2.290404328215695, 'delay3': -2.9010300292391653, 'delay4': -3.4717193201810517, 'delay5': -3.25252445823602, 'delay6': -4.516530611920254, 'delay7': 4.9284285833252515, 'fwhm1': 41.27121098912052, 'fwhm10': 38.22948474759549, 'fwhm11': 47.878667459196755, 'fwhm12': 29.112453834685567, 'fwhm13': 60.83498018261191, 'fwhm14': 36.24524338643347, 'fwhm15': 27.039066288272192, 'fwhm2': 48.31999214909398, 'fwhm3': 58.295268508029345, 'fwhm4': 40.60741884285142, 'fwhm5': 36.45053859504276, 'fwhm6': 26.56459259856799, 'fwhm7': 8.940508720962354, 'fwhm8': 31.053840903924705, 'fwhm9': 14.990183790698534, 'wavel1': 6166.023933133515, 'wavel10': 8883.12791301736, 'wavel11': 4274.506913232941, 'wavel12': 4896.168675410211, 'wavel13': 953.4538618811862, 'wavel14': 6384.780730490184, 
#'wavel15': 2329.8682414110053, 'wavel2': 7987.772674611483, 'wavel3': 3654.388850783153, 'wavel4': 1160.0036996037577, 'wavel5': 2404.443137988227, 'wavel6': 3415.0055910890787, 'wavel7': 2448.090524409101, 'wavel8': 7268.350488603589, 'wavel9': 9638.953866888804}}