#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:26:05 2019

@author: Carolina_Rossi
"""

#!/usr/bin/python

import numpy as np
import numpy.random as npr
import scipy as sp
import pylab as pl
import scipy.fftpack as spf
from scipy.ndimage import gaussian_filter

#%%
import os
#cwd = os.getcwd()
#os.chdir("/Users/Carolina_Rossi/Desktop/Y2_LABS/interferometry")
#cwn = os.getcwd()

#print(cwd, cwn)
fname = 'Data/Mercury/Hg_Yellow4.txt'
f=open(fname,'r') #here we open file and call it f

#created empty arrays to then fill them up
signal1=[]
signal2=[]
t_sec=[]
t_usec=[]
x=[]

"""A for loop is used for iterating over a sequence
execute a set of statements, once for each item in a list"""

#read in the data
lines=f.readlines()
#f.readlines() reads f until end of file  and returns a list containing the lines.
#we now create a variable line and iterate it over all lines
for line in range(len(lines)-1): #in range of the length of the lines variable (-1 to ignore last data point)
    signal1.append(int(lines[line].split()[0])) #appending the information from collumns to arrays
    signal2.append(int(lines[line].split()[1])) #split separates each element of a line and then we are appending each to one collumn
    t_sec.append(int(lines[line].split()[2])) #int is just to make it an integer rather than a string
    t_usec.append(int(lines[line].split()[3]))
    x.append(float(lines[line].split()[4]))

### Quite often the stage jumps at the beginning and so you may want to chop it off

s1=signal1[100:] #this is why we start from the sample 100
s2=signal2[100:]
p=x[100:]

#%%
"""
Interferogram corresponds to the Fourier transform of the original spectrum in terms of wavenumber.
Hence, manipulation needed to construct the original wavelength spectrum
'''
"""
# take a fourier transform
yf=spf.fft(s1)
#this is your signal 1
xf=spf.fftfreq(len(p))#second arg is sample spacing in seconds 1/f

# setting the correct x-axis for the fourier transform. Osciallations/step
#this is you stage position

#now some shifts to make plotting easier (google if interested)
xf=spf.fftshift(xf)
yf=spf.fftshift(yf)

#%%
dsamp=(abs(abs(x[-1])-abs(x[0]))/len(x))/1000 
tsamp=(abs(abs(p[-1])-abs(p[0]))/len(p))/1000
xx=xf[int(len(xf)/2+1):len(xf)]
repx= 2*tsamp/xx

# Plot parameters:
params = {
   'axes.labelsize': 25,
   'font.size': 25,
   'legend.fontsize': 25,
   'xtick.labelsize': 25,
   'ytick.labelsize': 25,
   'figure.figsize': [10,7]
   }

y = abs(yf[int(len(xf)/2+1):len(xf)]).tolist()
print('Central Wavelength',repx[y.index(max(y))])

pl.rcParams.update(params)
pl.rcParams["font.family"] = "Times New Roman"
pl.figure(3)
pl.title("Fourier Transform of the Hg Source with a Yellow Filter")
pl.xlabel("Wavelength (m)")
pl.ticklabel_format(style='sci', axis='x', scilimits=(-9,-9))#m,m to fix order of magnitude
pl.xlim(200e-9,1000e-8)
pl.ylabel("Relative Amplitude")
#pl.plot(repx, gaussian_filter(abs(yf[int(len(xf)/2+1):len(xf)], 25))
pl.plot(repx,abs(yf[int(len(xf)/2+1):len(xf)])/max(y), color='red') #map only half and take absolute value i.e. positive part of FT
np.savetxt("xtungstenft",repx)
np.savetxt("ytungstenft",abs(yf[int(len(xf)/2+1):len(xf)]))

half_max= max(y)/2
print(half_max)
y1= np.empty(len(repx))
y1.fill(half_max/max(y))

pl.plot(repx,y1) #Plotting half maximum
pl.show()