#imports
import numpy as np
from bayes_opt import BayesianOptimization
import matplotlib.pyplot as plt
import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
from subtargetfunctions import *
from field_synth_class import *
#from ErrorCorrectionFunction import *
from ErrorCorrectionFunction_integrate import *

#now import the code form the other files
import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
from subtargetfunctions import *
from bossfunction import *
from bossfunction_noplots import *
from field_synth_class import *
#from ErrorCorrectionFunction import * #out of date functions
from ErrorCorrectionFunction_integrate import *
import random
import statistics
###############################################################################################################################

#note: the time array must have the same spacing for the synthesiser and for the goal field!
t=np.linspace(0,100,10000)

###############################################################################################################################
#find mean of 5 random rms error outcomes
random_rms_l=[]
for i in range(5):
    CEP1=random.random()*2*np.pi
    CEP2=random.random()*2*np.pi
    CEP3=random.random()*2*np.pi

    amp1=random.random()
    amp2=random.random()
    amp3=random.random()

    delay2=random.random()*10-5
    delay3=random.random()*10-5

    wavel3=random.random()*1000+1100

    Field1_=Wavepacket(t0=50.0, wavel=400.0, fwhm=33.0, amp=amp1, CEP=CEP1)
    Field2_=Wavepacket(t0=50.0, wavel=775.0, fwhm=4.0, amp=amp2, CEP=CEP2)
    Field3_=Wavepacket(t0=50.0, wavel=wavel3, fwhm=45.0, amp=amp3, CEP=CEP3)

    pulses_=[Field1_,Field2_, Field3_]
    delays_=(delay2,delay3)
    #pass to synthesiser
    Synth_=Synthesiser(pulses_,delays_)

    E_rand=[]
    for i in range(len(t)):
        Ei=Synth_.E_field_value(i)
        E_rand.append(Ei)
    E_rand=np.array(E_rand)
    random_rms_l.append(maxIntens(t, E_rand))

random_rms=statistics.mean(random_rms_l)

##################################################################################################################################################
#run BO
#n_inits=np.array([0,2,4,6,8,10,12,14,16,18,20])
#n_iters=np.array([0,2,4,6,8,10,12,14,16,18,20])
#outcomes=np.zeros((11,11))

n_inits=np.array([1,2,3])
n_iters=np.array([1,2])
#outcomes shape:(iter,init)
outcomes=np.zeros((3,2))
#create fields


#parameters to be optimised
params=['CEP1','CEP2','CEP3','amp1','amp2','amp3','delay2','delay3','wavel3']
for i in range(len(n_inits)):
    for j in range(len(n_iters)):
        Field1=Wavepacket(t0=50.0, wavel=400.0, fwhm=33.0, amp=1.0, CEP=0.0)
        Field2=Wavepacket(t0=50.0, wavel=775.0, fwhm=4.0, amp=1.0, CEP=0.0)
        Field3=Wavepacket(t0=50.0, wavel=1100.0, fwhm=45.0, amp=1.0, CEP=0.0)
        #initialise pulse list and tuple of relative delays (from 1st pulse)
        pulses=[Field1,Field2, Field3]
        delays=(0,0)
        #pass to synthesiser
        Synth=Synthesiser(pulses,delays)
        BO_out,BO_res=BO_noplot(params, Synth, maxIntens, init_points=n_inits[i],n_iter=n_iters[j], t=t)
        outcomes[i][j]=BO_out["target"]/random_rms

###################################################################################################################
#plot outcome

plt.imshow(outcomes,extent=(n_iters[0],n_iters[-1],n_inits[0],n_inits[-1]),aspect = 'auto', origin="lower")
plt.xlabel("Iterations",fontsize=16)
plt.ylabel("Initial Points",fontsize=16)
cbar=plt.colorbar()
cbar.ax.set_ylabel('Ratio', rotation=270, labelpad=15,fontsize=16)
cbar.ax.tick_params(labelsize=14)
plt.title("Ratio optimised maximum intensity to random input",fontsize=20)
plt.show()

