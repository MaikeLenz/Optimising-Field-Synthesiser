import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
data = np.random.rand(4, 4)
fig, (ax1, ax2) = plt.subplots(2)
ax1.imshow(data)
ax1.set_title("Default colormap")
mpl.rc('image', cmap='Set2')
ax2.imshow(data)
ax2.set_title("Set default colormap")
plt.show()

plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)