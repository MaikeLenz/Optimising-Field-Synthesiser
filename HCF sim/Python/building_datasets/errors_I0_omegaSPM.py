import numpy as np

def I0_error(sigma_energy,sigma_lambda_rms_width,sigma_coupling,sigma_lambda0):
    return np.sqrt(sigma_energy**2+sigma_lambda_rms_width**2+sigma_coupling**2+8*sigma_lambda0**2)

def omega_SPM_error(sigma_energy,sigma_lambda_rms_width,sigma_coupling,sigma_lambda0, sigma_omega0, sigma_n2,sigma_tau):
    sigma_I0=I0_error(sigma_energy,sigma_lambda_rms_width,sigma_coupling,sigma_lambda0)
    return np.sqrt(sigma_I0**2+sigma_omega0**2+sigma_n2**2+sigma_tau**2)

print(I0_error(0.1,0.01,0.05,0.1))
print(omega_SPM_error(0.1,0.01,0.1,0.1,0.1,0.1+0.25/9.30,0.51))