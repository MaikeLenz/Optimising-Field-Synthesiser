import PIL as PIL
import matplotlib.pyplot as plt
import numpy as np
#%%
# Analysis of quantitative measurements
# Open images and check sizes

#damaged side of Forces window

im1 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\initial\\7_09.PNG')
im2 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\initial\\8_06.PNG')
im3 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\initial\\8_47.PNG')
im4 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\initial\\12_35.PNG')
imB = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\initial\\Background.PNG')
images = [im1,im2,im3, im4]

imB_array =np.asarray(imB.convert('L'))
imB_array =imB_array.astype(np.int16)

f = plt.figure(constrained_layout=True)
gs = f.add_gridspec(3,4)
slicing=[600,1100,900,1500]

for i in range(len(images)):
    im_array= np.asarray(images[i].convert('L'))
    im_array=im_array.astype(np.int16)
    newimage2_array=im_array-imB_array
    newimage2_array=newimage2_array[slicing[0]:slicing[1],slicing[2]:slicing[3]] #slice image to only contain the interesting part

    max=40
    min=-5
    if i >=0 and i<4:
        f_ax = f.add_subplot(gs[0,i])
        im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        #f.colorbar(im)
    elif i>=4 and i<8:
        f_ax = f.add_subplot(gs[1, i-4])
        im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        #f.colorbar(im)
    elif i>=8 and i<12:
        f_ax = f.add_subplot(gs[2, i-8])
        im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        #f.colorbar(im)
    elif i>=12 and i<16:
        f_ax = f.add_subplot(gs[3, i-12])
        im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        #f.colorbar(im)
f.subplots_adjust(right=0.8)
cbar_ax = f.add_axes([0.85, 0.15, 0.015, 0.7])
f.colorbar(im, cax=cbar_ax)
plt.suptitle("Initial Force Measurements")
plt.show()
"""
#plt.figure()
y_shift = 1/(0.006*13.4615)
#y_shift = 0
pixel_size = 0.006
beam_size_large = 10.5
beam_size_small = 0.78
magnification = beam_size_large/beam_size_small
scaling = pixel_size*magnification

crop_size = [180,300,250,450]

for i in range(len(images)):
    newimage2_array=np.asarray(images[i].convert('L'))-np.asarray(imB.convert('L'))

    newimage2_array=newimage2_array[crop_size[0]:crop_size[1],crop_size[2]:crop_size[3]]
    
    # Shift by 1mm*i
    amount_taken_off = len(newimage2_array) - int(y_shift*i)
    if amount_taken_off < 0:
        pass
    else:
        length = len(newimage2_array[0])
        newimage2_array = newimage2_array[int(y_shift*i):]
        newimage2_array = np.append(np.zeros((amount_taken_off, length)),newimage2_array, axis=0)
        #print(newimage2_array)
        plt.imshow(newimage2_array, cmap='inferno', alpha=0.15, extent=[crop_size[2]*scaling,crop_size[3]*scaling,crop_size[0]*scaling,crop_size[1]*scaling])

plt.show()
"""