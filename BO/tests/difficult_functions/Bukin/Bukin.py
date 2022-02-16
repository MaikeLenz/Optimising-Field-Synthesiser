import numpy as np
import matplotlib.pyplot as plt

def func(x, y):
    """
    returns the negative of the Bukin function
    """
    return -(100*np.sqrt(np.abs(y-0.01*x**2))+0.01*np.abs(x+10))

# generate 2 2d grids for the x & y bounds
y, x = np.meshgrid(np.linspace(-2, 2, 200), np.linspace(-2, 2, 200))
#z as a function of x and y
z=((1+((x+y+1)**2)*(19-14*x+3*x**2-14*y+6*x*y+3*y**2))*(30+((2*x-3*y)**2)*(18-32*x+12*x**2+48*y-36*x*y+27*y**2)))
#z = (1+(x+y+1)**2*(19-14*x+3*x**2-14*y+6*x*y+3*y**2))*(30+(2*x-3*y)**2*(18-32*x+12*x**2+48*y-36*x*y+27*y**2))  

# x and y are bounds, so z should be the value *inside* those bounds.
# Therefore, remove the last value from the z array.
z = z[:-1, :-1]
z_min, z_max = -np.abs(z).max(), np.abs(z).max()

fig, ax = plt.subplots()

#c = ax.pcolormesh(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
c = ax.pcolormesh(x, y, z, vmin=z_min, vmax=z_max)

ax.set_title('Bukin')
# set the limits of the plot to the limits of the data
ax.axis([x.min(), x.max(), y.min(), y.max()])
fig.colorbar(c, ax=ax)

plt.show()