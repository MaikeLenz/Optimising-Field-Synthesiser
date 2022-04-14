import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16

fig, axs = plt.subplots(2,2)

def Ackley(x, y):
    """
    returns the negative of the Ackley function
    """
    return -(-20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2)))-np.exp(0.5 * (np.cos(2 * np.pi * x)+np.cos(2 * np.pi * y))) + np.e + 20)

y, x = np.meshgrid(np.linspace(-5, 5, 200), np.linspace(-5, 5, 200))
z = -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2)))-np.exp(0.5 * (np.cos(2 * np.pi * x)+np.cos(2 * np.pi * y))) + np.e + 20
z = z[:-1, :-1]
z_min, z_max = -np.abs(z).max(), np.abs(z).max()

c = axs[0,0].pcolormesh(x, y, z, vmin=0, vmax=z_max)
axs[0,0].set_title('Ackley', size=24)
axs[0,0].axis([x.min(), x.max(), y.min(), y.max()])
fig.colorbar(c, ax=axs[0,0])

def Booth(x, y):
    """
    negative of the Rastrigin function
    BO maximises but the Rastrigin function has a global minimum
    """
    return  - (x+2*y-7)**2 - (2*x+y-5)**2
y, x = np.meshgrid(np.linspace(-10, 10, 200), np.linspace(-10, 10, 200))
z = (x+2*y-7)**2 + (2*x+y-5)**2
z = z[:-1, :-1]
z_min, z_max = -np.abs(z).max(), np.abs(z).max()

c = axs[0,1].pcolormesh(x, y, z, vmin=0, vmax=z_max)
axs[0,1].set_title('Booth', size=24)
axs[0,1].axis([x.min(), x.max(), y.min(), y.max()])
fig.colorbar(c, ax=axs[0,1])

def Matyas(x, y):
    """
    negative of the Rastrigin function
    BO maximises but the Rastrigin function has a global minimum
    """
    return  - (0.26*(x**2+y**2)-0.48*x*y)
y, x = np.meshgrid(np.linspace(-10, 10, 200), np.linspace(-10, 10, 200))
z = (0.26*(x**2+y**2)-0.48*x*y)
z = z[:-1, :-1]
z_min, z_max = -np.abs(z).max(), np.abs(z).max()

c = axs[1,0].pcolormesh(x, y, z, vmin=0, vmax=z_max)
axs[1,0].set_title('Matyas', size=24)
axs[1,0].axis([x.min(), x.max(), y.min(), y.max()])
fig.colorbar(c, ax=axs[1,0])

def Sphere(x, y):
    """
    returns the negative of the sphere function
    """
    return -(x**2+y**2)
y, x = np.meshgrid(np.linspace(-5, 5, 200), np.linspace(-5, 5, 200))
z = (x**2+y**2)
z = z[:-1, :-1]
z_min, z_max = -np.abs(z).max(), np.abs(z).max()

c = axs[1,1].pcolormesh(x, y, z, vmin=0, vmax=z_max)
axs[1,1].set_title('Sphere', size=24)
axs[1,1].axis([x.min(), x.max(), y.min(), y.max()])
fig.colorbar(c, ax=axs[1,1])

plt.show()