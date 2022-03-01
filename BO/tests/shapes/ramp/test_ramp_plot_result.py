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

BO_output={'target': -0.015916135188874022, 'params': {'CEP1': 3.628093045537061, 'CEP10': 6.135261896897698, 'CEP11': 5.173800421987468, 'CEP12': 0.7360425382219573, 'CEP13': 3.167016317099395, 'CEP14': 4.960890177001713, 'CEP15': 2.0002565843537656, 'CEP2': 4.507845766241029, 'CEP3': 2.510210843069925, 'CEP4': 4.51329077374211, 'CEP5': 5.664857071331409, 'CEP6': 3.3664806938373935, 'CEP7': 0.419640536385667, 'CEP8': 1.4642418284158556, 'CEP9': 6.052386830558784, 'amp1': 0.45221702019165144, 'amp10': 0.6675151804260606, 'amp11': 0.503765395987246, 'amp12': 0.6838868866567267, 'amp13': 0.5529210356592198, 'amp14': 0.15385067279518894, 'amp15': 0.2067906925155013, 'amp2': 0.8554378451787152, 'amp3': 0.6859760783900335, 'amp4': 0.40333053862182855, 'amp5': 0.6592939967709974, 'amp6': 0.9996870300239953, 'amp7': 0.707896042847706, 'amp8': 0.705148042827909, 'amp9': 0.9990217672965653, 'fwhm1': 7.953043416421451, 'fwhm10': 22.698036564901333, 'fwhm11': 6.7451473713601064, 'fwhm12': 39.84753007251638, 'fwhm13': 49.11157105766848, 'fwhm14': 24.542758179757104, 'fwhm15': 32.321943591600366, 'fwhm2': 34.20805432161419, 'fwhm3': 37.02969691758366, 'fwhm4': 6.389786506216618, 'fwhm5': 33.696208653578566, 'fwhm6': 18.837990888445646, 'fwhm7': 62.041365178420385, 'fwhm8': 22.703034236536798, 'fwhm9': 19.558367009253452, 'wavel1': 2652.6900878973584, 'wavel10': 5375.867320862984, 'wavel11': 5810.818243270944, 'wavel12': 5344.066237799297, 'wavel13': 6924.836609207718, 'wavel14': 9537.61215454602, 'wavel15': 7956.795760550585, 'wavel2': 4810.102397793363, 'wavel3': 8327.446371304712, 'wavel4': 2713.1704760381726, 'wavel5': 9524.59606723532, 'wavel6': 4531.228807214087, 'wavel7': 7449.82770738779, 'wavel8': 8238.592080561051, 'wavel9': 4249.556262453723}}

#create fields
Field1=Wavepacket(t0=50.0, wavel=BO_output["params"]["wavel1"], fwhm=BO_output["params"]["fwhm1"], amp=BO_output["params"]["amp1"], CEP=BO_output["params"]["CEP1"])
Field2=Wavepacket(t0=50.0, wavel=BO_output["params"]["wavel2"], fwhm=BO_output["params"]["fwhm2"], amp=BO_output["params"]["amp2"], CEP=BO_output["params"]["CEP2"])
Field3=Wavepacket(t0=50.0, wavel=BO_output["params"]["wavel3"], fwhm=BO_output["params"]["fwhm3"], amp=BO_output["params"]["amp3"], CEP=BO_output["params"]["CEP3"])
Field4=Wavepacket(t0=50.0, wavel=BO_output["params"]["wavel4"], fwhm=BO_output["params"]["fwhm4"], amp=BO_output["params"]["amp4"], CEP=BO_output["params"]["CEP4"])
Field5=Wavepacket(t0=50.0, wavel=BO_output["params"]["wavel5"], fwhm=BO_output["params"]["fwhm5"], amp=BO_output["params"]["amp5"], CEP=BO_output["params"]["CEP5"])
Field6=Wavepacket(t0=50.0, wavel=BO_output["params"]["wavel6"], fwhm=BO_output["params"]["fwhm6"], amp=BO_output["params"]["amp6"], CEP=BO_output["params"]["CEP6"])
Field7=Wavepacket(t0=50.0, wavel=BO_output["params"]["wavel7"], fwhm=BO_output["params"]["fwhm7"], amp=BO_output["params"]["amp7"], CEP=BO_output["params"]["CEP7"])
Field8=Wavepacket(t0=50.0, wavel=BO_output["params"]["wavel8"], fwhm=BO_output["params"]["fwhm8"], amp=BO_output["params"]["amp8"], CEP=BO_output["params"]["CEP8"])
Field9=Wavepacket(t0=50.0, wavel=BO_output["params"]["wavel9"], fwhm=BO_output["params"]["fwhm9"], amp=BO_output["params"]["amp9"], CEP=BO_output["params"]["CEP9"])
Field10=Wavepacket(t0=50.0, wavel=BO_output["params"]["wavel10"], fwhm=BO_output["params"]["fwhm10"], amp=BO_output["params"]["amp10"], CEP=BO_output["params"]["CEP10"])
Field11=Wavepacket(t0=50.0, wavel=BO_output["params"]["wavel11"], fwhm=BO_output["params"]["fwhm11"], amp=BO_output["params"]["amp11"], CEP=BO_output["params"]["CEP11"])
Field12=Wavepacket(t0=50.0, wavel=BO_output["params"]["wavel12"], fwhm=BO_output["params"]["fwhm12"], amp=BO_output["params"]["amp12"], CEP=BO_output["params"]["CEP12"])
Field13=Wavepacket(t0=50.0, wavel=BO_output["params"]["wavel13"], fwhm=BO_output["params"]["fwhm13"], amp=BO_output["params"]["amp13"], CEP=BO_output["params"]["CEP13"])
Field14=Wavepacket(t0=50.0, wavel=BO_output["params"]["wavel14"], fwhm=BO_output["params"]["fwhm14"], amp=BO_output["params"]["amp14"], CEP=BO_output["params"]["CEP14"])
Field15=Wavepacket(t0=50.0, wavel=BO_output["params"]["wavel15"], fwhm=BO_output["params"]["fwhm15"], amp=BO_output["params"]["amp15"], CEP=BO_output["params"]["CEP15"])
#initialise pulse list and tuple of relative delays (from 1st pulse)
pulses=[Field1,Field2, Field3, Field4, Field5,Field6,Field7,Field8,Field9,Field10,Field11,Field12,Field13,Field14,Field15]
delays=(0,0,0,0,0,0,0,0,0,0,0,0,0,0)
#pass to synthesiser
Synth=Synthesiser(pulses,delays)

#define goal field
def ramp(x,a):
    return a*x
#note: the time array must have the same spacing for the synthesiser and for the goal field!
t=np.linspace(0,100,10000)
#we want 30fs, so this is fraction of the whole t array
t_goal=t[:int((30/100)*10000)]
print(len(t_goal))
I_goal=ramp(t_goal,12/30)

#parameters to be optimised
params=['wavel1']
BO(params, Synth, errorCorrectionAdvanced_int, 0,0, t=t,goal_field=I_goal)

#outcome
#{'target': -0.015916135188874022, 'params': {'CEP1': 3.628093045537061, 'CEP10': 6.135261896897698, 'CEP11': 5.173800421987468, 'CEP12': 0.7360425382219573, 'CEP13': 3.167016317099395, 'CEP14': 4.960890177001713, 'CEP15': 2.0002565843537656, 'CEP2': 4.507845766241029, 'CEP3': 2.510210843069925, 'CEP4': 4.51329077374211, 'CEP5': 5.664857071331409, 'CEP6': 3.3664806938373935, 'CEP7': 0.419640536385667, 'CEP8': 1.4642418284158556, 'CEP9': 6.052386830558784, 'amp1': 0.45221702019165144, 'amp10': 0.6675151804260606, 'amp11': 0.503765395987246, 'amp12': 0.6838868866567267, 'amp13': 0.5529210356592198, 'amp14': 0.15385067279518894, 'amp15': 0.2067906925155013, 'amp2': 0.8554378451787152, 'amp3': 0.6859760783900335, 'amp4': 0.40333053862182855, 'amp5': 0.6592939967709974, 'amp6': 0.9996870300239953, 'amp7': 0.707896042847706, 'amp8': 0.705148042827909, 'amp9': 0.9990217672965653, 'fwhm1': 7.953043416421451, 'fwhm10': 22.698036564901333, 'fwhm11': 6.7451473713601064, 'fwhm12': 39.84753007251638, 'fwhm13': 49.11157105766848, 'fwhm14': 24.542758179757104, 'fwhm15': 32.321943591600366, 'fwhm2': 34.20805432161419, 'fwhm3': 37.02969691758366, 'fwhm4': 6.389786506216618, 'fwhm5': 33.696208653578566, 'fwhm6': 18.837990888445646, 'fwhm7': 62.041365178420385, 'fwhm8': 22.703034236536798, 'fwhm9': 19.558367009253452, 'wavel1': 
#2652.6900878973584, 'wavel10': 5375.867320862984, 'wavel11': 5810.818243270944, 'wavel12': 5344.066237799297, 'wavel13': 6924.836609207718, 'wavel14': 9537.61215454602, 'wavel15': 7956.795760550585, 'wavel2': 4810.102397793363, 'wavel3': 8327.446371304712, 'wavel4': 2713.1704760381726, 'wavel5': 9524.59606723532, 'wavel6': 4531.228807214087, 'wavel7': 7449.82770738779, 'wavel8': 8238.592080561051, 'wavel9': 4249.556262453723}}
