import numpy as np
import sympy as sym
import scipy as sp
#from refractiveindex.info, fused silica:
def n(x):
    """
    unitless, x=wavelength in microns
    """
    return (1+0.6961663/(1-(0.0684043/x)**2)+0.4079426/(1-(0.1162414/x)**2)+0.8974794/(1-(9.896161/x)**2))**.5
x=sym.Symbol('x')
dn_x = sym.diff(n(x))
#print(dn_x)
c=299792458 #m/s

def L(CEPshift, x0):
    """
    returns L in microns
    """
    expr=dn_x
    print(expr.subs({x:x0}))
    return (-CEPshift/(2*np.pi))/(expr.subs({x:x0}))

print(L(np.pi,0.78))