import numpy as np
import random as rd
import matplotlib.pyplot as plt
import plotparams
"""
#import julia, the api module
import julia

#Set the location for the julia excutable (if need be)
julia.Julia(runtime="C:\\Users\\gabri\\AppData\\Local\\Programs\\Julia-1.5.4\\bin\\julia.exe")

#julia.Main is used to add and access atributes to the julia namespace
#inside Main.eval(), don't need Main.<atribute>, can just access via <attribute>
from julia import Main

"""
import julia
#from julia.api import Julia


julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin")

from julia import Main

#Main.eval() runs julia code.
#Main.using("TextAnalysis") #- imports Julia packages needed in .jl if need be


####
#Running julia in python directly
####

#define the data in python
data1=[1,2,3,4,5]

#define the data in the julia-readable object julia.Main
Main.data_j1 = data1

#define a julia function
Main.eval('func(x) = x^2')

#run and return the values back to a python object
out1 = Main.eval("func.(data_j1)")

print("out1 = ", out1)
print("type of out1 = ", type(out1))


####
#Running a julia file in python
####
data2= np.linspace(-100,100,1000)
Main.data_j2 = data2

Main.eval('include("Playground.jl")')
out2 = Main.eval("quad.(data_j2)")

print("out2[0:10] = ", out2[0:10])
print("type of out2 = ", type(out2))

plt.plot(data2, out2)
plt.ylim(0, 10100)
plt.grid()
plt.show()