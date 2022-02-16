import numpy as np
import matplotlib.pyplot as plt

def func(x, y):
    """
    returns the negative of the Ackley function
    """
    return -(-20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2)))-np.exp(0.5 * (np.cos(2 * np.pi * x)+np.cos(2 * np.pi * y))) + np.e + 20)

# generate 2 2d grids for the x & y bounds
y, x = np.meshgrid(np.linspace(-5, 5, 200), np.linspace(-5, 5, 200))
#z as a function of x and y
z = -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2)))-np.exp(0.5 * (np.cos(2 * np.pi * x)+np.cos(2 * np.pi * y))) + np.e + 20

# x and y are bounds, so z should be the value *inside* those bounds.
# Therefore, remove the last value from the z array.
z = z[:-1, :-1]
z_min, z_max = -np.abs(z).max(), np.abs(z).max()

fig, ax = plt.subplots()

#c = ax.pcolormesh(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
c = ax.pcolormesh(x, y, z, vmin=z_min, vmax=z_max)

ax.set_title('Ackley')
# set the limits of the plot to the limits of the data
ax.axis([x.min(), x.max(), y.min(), y.max()])
fig.colorbar(c, ax=ax)

plt.show()