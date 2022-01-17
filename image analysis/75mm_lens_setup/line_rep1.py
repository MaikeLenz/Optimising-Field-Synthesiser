import PIL as PIL
import matplotlib.pyplot as plt
import numpy as np
#%%
# Analysis of quantitative measurements
# Open images and check sizes

#damaged side of chip window

im1 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Line\\0.png')
im2 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Line\\4.png')
im3 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Line\\8.png')
im4 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Line\\12.png')

im5 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Line\\16.png')
im6 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Line\\20.png')
im7 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Line\\24.png')

im8 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Line\\27.png')
im9 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Line\\End.png')

imB = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\repeat 1\\Line\\Background.png')
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
    max=3
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
plt.suptitle("Lined window, 4mm increments")
f.colorbar(im, cax=cbar_ax)
plt.show()
