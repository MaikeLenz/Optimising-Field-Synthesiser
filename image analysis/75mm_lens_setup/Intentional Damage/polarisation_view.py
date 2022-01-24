import PIL as PIL
import matplotlib.pyplot as plt
import numpy as np
#%%
# display background subtractions of all damages

im1 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\Intentional Damage\\Polarisation\\50.PNG')
im2 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\Intentional Damage\\Polarisation\\100down.PNG')
im3 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\Intentional Damage\\Polarisation\\100up.PNG')
im4 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\Intentional Damage\\Polarisation\\200.PNG')
im5 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\Intentional Damage\\Polarisation\\300.PNG')
im6 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\Intentional Damage\\Polarisation\\400.PNG')
im7 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\Intentional Damage\\Polarisation\\500.PNG')
im8 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\Intentional Damage\\Polarisation\\600.PNG')
im9 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\Intentional Damage\\Polarisation\\700.PNG')
im10 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\Intentional Damage\\Polarisation\\800_wiped.PNG')
im11 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\Intentional Damage\\Polarisation\\900_wiped.PNG')
im12 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\Intentional Damage\\Polarisation\\1000.PNG')

imB = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\Intentional Damage\\Polarisation\\Background.PNG')
images = [im1,im2,im3, im4, im5, im6, im7, im8, im9,im10,im11,im12]


imB_array =np.asarray(imB.convert('L'))
imB_array =imB_array.astype(np.int16)

f = plt.figure(constrained_layout=True)
layout=[3,4]
gs = f.add_gridspec(layout[0],layout[1])

for i in range(len(images)):
    im_array= np.asarray(images[i].convert('L'))
    im_array=im_array.astype(np.int16)
    newimage2_array=im_array-imB_array

    #newimage2_array=newimage2_array[600:1000,900:1300]
    max=10
    min=-5
    if i >=0 and i<layout[1]:
        f_ax = f.add_subplot(gs[0,i])
        #im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        im=f_ax.imshow(newimage2_array, cmap='gray')
    elif i<2*layout[1]:
        f_ax = f.add_subplot(gs[1, i-layout[1]])
        #im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        im=f_ax.imshow(newimage2_array, cmap='gray')
    elif i<3*layout[1]:
        f_ax = f.add_subplot(gs[2, i-2*layout[1]])
        im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        #im=f_ax.imshow(newimage2_array, cmap='gray')
f.subplots_adjust(right=0.8)
cbar_ax = f.add_axes([0.85, 0.15, 0.015, 0.7])
plt.suptitle("Polarisation view, Intentional damage")
f.colorbar(im, cax=cbar_ax)
plt.show()
