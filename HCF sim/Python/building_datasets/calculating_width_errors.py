import pandas as pd
import numpy as np

# delta_omega_rms
# Read input pulse params
df = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\HCF_scans\\power in\\extracted_params.csv")
powers = df.iloc[:,0]
energies = powers/1000
λ0s = df.iloc[:,1]
domegas = df.iloc[:,2]

domega_std = np.std(domegas)
domega_mean = np.mean(domegas)
domega_percentage_err = domega_std/domega_mean

print(domega_percentage_err)