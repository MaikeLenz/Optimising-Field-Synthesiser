import PIL as PIL
import matplotlib.pyplot as plt
import numpy as np
#%%
# Analysis of quantitative measurements
# Open images and check sizes


im1 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\clamped_bottom\\Window.PNG')


imB = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\clamped_bottom\\Background.PNG')
images = [im1]

imB_array =np.asarray(imB.convert('L'))
imB_array =imB_array.astype(np.int16)

imsub_array =np.asarray(imB.convert('L'))
imsub_array =imsub_array.astype(np.int16)
slicing=[700,1000,1000,1400]

im_height=slicing[1]-slicing[0]
slice_height=10


for i in range(len(images)):
    im_array= np.asarray(images[i].convert('L'))
    im_array=im_array.astype(np.int16)
    newimage2_array=im_array-imsub_array
    newimage2_array=newimage2_array[slicing[0]:slicing[1],slicing[2]:slicing[3]]

    max=10
    min=-2
    im=plt.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        #im=f_ax.plot(x,avg_slice)
#f.subplots_adjust(right=0.8)
#cbar_ax = plt.add_axes([0.85, 0.15, 0.015, 0.7])
plt.suptitle("Undamaged window, Clamped Bottom")
plt.colorbar(im)
plt.show()
