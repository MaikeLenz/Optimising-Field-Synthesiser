"""
Plot parameters module
"""

import matplotlib.pyplot as plt

params = {
    "axes.labelsize":35,
    "font.size":30,
    "legend.fontsize":30,
    "xtick.labelsize":30,
    "ytick.labelsize":30,
    "figure.figsize": [15,15],
}
plt.rcParams.update(params)