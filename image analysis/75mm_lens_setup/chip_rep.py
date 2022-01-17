import PIL as PIL
import matplotlib.pyplot as plt
import numpy as np
#%%
# Analysis of quantitative measurements
# Open images and check sizes

#damaged side of chip window

im1 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Chip\\0.PNG')
im2 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Chip\\4.PNG')
im3 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Chip\\8.PNG')
im4 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Chip\\12.PNG')

im5 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Chip\\16.PNG')
im6 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Chip\\20.PNG')
im7 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Chip\\24.PNG')

im8 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Chip\\27.PNG')
im9 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Chip\\End.PNG')

imB = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Chip\\Background.PNG')
images = [im1,im2,im3, im4, im5, im6, im7, im8, im9]


imB_array =np.asarray(imB.convert('L'))
imB_array =imB_array.astype(np.int16)

f = plt.figure(constrained_layout=True)
gs = f.add_gridspec(3,3)

for i in range(len(images)):
    im_array= np.asarray(images[i].convert('L'))
    im_array=im_array.astype(np.int16)
    newimage2_array=im_array-imB_array

    #newimage2_array=newimage2_array[600:1000,900:1300]
    max=30
    min=-5
    if i >=0 and i<3:
        f_ax = f.add_subplot(gs[0,i])
        im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        #f.colorbar(im)
    elif i<6:
        f_ax = f.add_subplot(gs[1, i-3])
        im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        #f.colorbar(im)
    elif i<9:
        f_ax = f.add_subplot(gs[2, i-6])
        im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        #f.colorbar(im)
f.subplots_adjust(right=0.8)
cbar_ax = f.add_axes([0.85, 0.15, 0.015, 0.7])
plt.suptitle("Chip window, 4mm increments")
f.colorbar(im, cax=cbar_ax)
plt.show()
