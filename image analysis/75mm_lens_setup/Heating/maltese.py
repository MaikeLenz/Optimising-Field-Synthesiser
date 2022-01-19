import PIL as PIL
import matplotlib.pyplot as plt
import numpy as np

im1 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\Heating\\test6_cameraface.png')
imB = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\Heating\\Background.png')
images = [im1]

imB_array =np.asarray(imB.convert('L'))
imB_array =imB_array.astype(np.int16)

f = plt.figure(constrained_layout=True)
gs = f.add_gridspec(1,1)

im_array= np.asarray(images[0].convert('L'))
im_array=im_array.astype(np.int16)
newimage2_array=im_array-imB_array

#newimage2_array=newimage2_array[600:1000,900:1300]
max=50
min=-5

f_ax = f.add_subplot(gs[0,0])
im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
f.subplots_adjust(right=0.8)
cbar_ax = f.add_axes([0.85, 0.15, 0.015, 0.7])
plt.suptitle("Maltese Cross")
f.colorbar(im, cax=cbar_ax)
plt.show()