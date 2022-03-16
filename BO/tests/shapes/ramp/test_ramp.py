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
def ramp(x,a):
    return a*x
#note: the time array must have the same spacing for the synthesiser and for the goal field!
t=np.linspace(0,100,10000)
#we want 30fs, so this is fraction of the whole t array
t_goal=t[:int((10/100)*10000)]
print(len(t_goal))
E_goal=ramp(t_goal,1)

#parameters to be optimised
params=['wavel1','wavel2','wavel3','wavel4','wavel5','wavel6','wavel7','wavel8','wavel9','wavel10','wavel11','wavel12','wavel13','wavel14','wavel15',
'CEP1','CEP2','CEP3','CEP4','CEP5','CEP6','CEP7','CEP8','CEP9','CEP10','CEP11','CEP12','CEP13','CEP14','CEP15',
'fwhm1','fwhm2','fwhm3','fwhm4','fwhm5','fwhm6','fwhm7','fwhm8','fwhm9','fwhm10','fwhm11','fwhm12','fwhm13','fwhm14','fwhm15',
'amp1','amp2','amp3','amp4','amp5','amp6','amp7','amp8','amp9','amp10','amp11','amp12','amp13','amp14','amp15']
BO(params, Synth, errorCorrectionAdvanced_int, 10,500, t=t,goal_field=E_goal,field_to_shape="E")

#outcome
#{'target': -0.015916135188874022, 'params': {'CEP1': 3.628093045537061, 'CEP10': 6.135261896897698, 'CEP11': 5.173800421987468, 'CEP12': 0.7360425382219573, 'CEP13': 3.167016317099395, 'CEP14': 4.960890177001713, 'CEP15': 2.0002565843537656, 'CEP2': 4.507845766241029, 'CEP3': 2.510210843069925, 'CEP4': 4.51329077374211, 'CEP5': 5.664857071331409, 'CEP6': 3.3664806938373935, 'CEP7': 0.419640536385667, 'CEP8': 1.4642418284158556, 'CEP9': 6.052386830558784, 'amp1': 0.45221702019165144, 'amp10': 0.6675151804260606, 'amp11': 0.503765395987246, 'amp12': 0.6838868866567267, 'amp13': 0.5529210356592198, 'amp14': 0.15385067279518894, 'amp15': 0.2067906925155013, 'amp2': 0.8554378451787152, 'amp3': 0.6859760783900335, 'amp4': 0.40333053862182855, 'amp5': 0.6592939967709974, 'amp6': 0.9996870300239953, 'amp7': 0.707896042847706, 'amp8': 0.705148042827909, 'amp9': 0.9990217672965653, 'fwhm1': 7.953043416421451, 'fwhm10': 22.698036564901333, 'fwhm11': 6.7451473713601064, 'fwhm12': 39.84753007251638, 'fwhm13': 49.11157105766848, 'fwhm14': 24.542758179757104, 'fwhm15': 32.321943591600366, 'fwhm2': 34.20805432161419, 'fwhm3': 37.02969691758366, 'fwhm4': 6.389786506216618, 'fwhm5': 33.696208653578566, 'fwhm6': 18.837990888445646, 'fwhm7': 62.041365178420385, 'fwhm8': 22.703034236536798, 'fwhm9': 19.558367009253452, 'wavel1': 
#2652.6900878973584, 'wavel10': 5375.867320862984, 'wavel11': 5810.818243270944, 'wavel12': 5344.066237799297, 'wavel13': 6924.836609207718, 'wavel14': 9537.61215454602, 'wavel15': 7956.795760550585, 'wavel2': 4810.102397793363, 'wavel3': 8327.446371304712, 'wavel4': 2713.1704760381726, 'wavel5': 9524.59606723532, 'wavel6': 4531.228807214087, 'wavel7': 7449.82770738779, 'wavel8': 8238.592080561051, 'wavel9': 4249.556262453723}}

#with Eabs:
#{'target': -0.03160267675950903, 'params': {'CEP1': 5.081734737046827, 'CEP10': 6.065892743307488, 'CEP11': 2.3494191359625676, 'CEP12': 0.18236669016790294, 'CEP13': 0.9836695997345528, 'CEP14': 5.771816516340279, 'CEP15': 0.375337749606135, 'CEP2': 6.159784314250184, 'CEP3': 0.881969398317953, 'CEP4': 5.069665183026286, 'CEP5': 3.902740071766045, 'CEP6': 3.068707666862539, 'CEP7': 2.442176560762687, 'CEP8': 4.067679558322259, 'CEP9': 2.409496263479665, 'amp1': 0.3553576653165771, 'amp10': 0.40545426336956336, 'amp11': 0.33849941209886986, 'amp12': 0.7442792957325794, 'amp13': 0.9311842531792183, 'amp14': 0.8899115394368816, 'amp15': 0.5735342263442911, 'amp2': 0.9693187945105298, 'amp3': 0.6395678074999824, 'amp4': 0.4654491673417631, 'amp5': 0.24390518241837691, 'amp6': 0.9008741193334369, 'amp7': 0.14006188980909356, 'amp8': 0.8451910654834339, 'amp9': 0.301790832344377, 'fwhm1': 33.65795790694159, 'fwhm10': 65.2675937660529, 'fwhm11': 23.547812846138854, 'fwhm12': 14.341492703100672, 'fwhm13': 15.18942803538096, 'fwhm14': 25.790927710594744, 'fwhm15': 20.11199562197598, 'fwhm2': 24.121356045167353, 'fwhm3': 32.38051330486604, 'fwhm4': 43.133345548428785, 'fwhm5': 52.53670151345022, 'fwhm6': 24.865433297301987, 'fwhm7': 55.82632951991561, 'fwhm8': 17.76426703589764, 'fwhm9': 36.6399570950194, 'wavel1': 1706.0695360822747, 'wavel10': 1200.8090350107932, 'wavel11': 1794.2170063818312, 'wavel12': 1414.941426454903, 'wavel13': 1306.2897044198987, 'wavel14': 1930.6434533510767, 'wavel15': 670.833846424995, 'wavel2': 1388.872129322187, 'wavel3': 1115.7642189734556, 'wavel4': 1322.1414305812, 'wavel5': 1690.2162228215327, 'wavel6': 1343.852634491258, 'wavel7': 437.8614893364089, 'wavel8': 1930.2072645620087, 'wavel9': 1628.3164203431957}}