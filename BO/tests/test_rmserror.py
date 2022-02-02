import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
from ErrorCorrectionFunction_integrate import *
import numpy as np

#test rms error by inputting the same field twice, shoud return zero

def gauss(w,A,u,o):
    return A*np.exp(-((w-u)**2)/o**2)

t=np.linspace(0,100,1000)
I1=gauss(t,1,50,10)
I2=I1

#same function, so rms error should be zero
print(errorCorrection_int(t,I1,I2))
#yes,returns zero

#Now: test advanced error correction
#shift I2 and scale it up
I3=gauss(t,2,60,10)
print(errorCorrectionAdvanced_int(t,I1,I3))
#returns 0.03, v small, close to zero -> shifting works

#to compare: what would their rms error be without shifting or scaling?
print(errorCorrection_int(t,I1,I3))
#returns 5.7 so the correction made a big difference!
