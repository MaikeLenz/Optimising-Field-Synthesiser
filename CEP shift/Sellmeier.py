
#from refractiveindex.info, fused silica:
def n(x):
    return n=(1+0.6961663/(1-(0.0684043/x)**2)+0.4079426/(1-(0.1162414/x)**2)+0.8974794/(1-(9.896161/x)**2))**.5

dn_omega = dn_x*dx_omega
CEPshift=(omega**2/c)*dn_omega*L