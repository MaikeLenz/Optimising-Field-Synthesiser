import numpy as np
import matplotlib.pyplot as plt
import PIL as PIL

#take image 9 of the line transmission and inverse FT
"""
img = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\5.PNG')
imB = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\Background.PNG')
"""

#high force clamping
img= PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\5_08ohms\\14.PNG')
imB = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\5_08ohms\\Background.PNG')

imB_array =np.asarray(imB.convert('L'))
imB_array =imB_array.astype(np.int16)

im_array= np.asarray(img.convert('L'))
im_array=im_array.astype(np.int16)
newimage_array=im_array-imB_array
slicing=[650,820,900,1100]
#newimage_array=newimage_array[slicing[0]:slicing[1],slicing[2]:slicing[3]]
centre=[-slicing[0]+slicing[1],-slicing[2]+slicing[3]]

inv= np.fft.ifftshift(np.fft.ifft2(newimage_array)) #inverse FT and shift zero freq components to centre
#inv= np.fft.ifft2(newimage_array)
inv = np.log(np.abs(inv))
#inv[inv > 255] = 255

#ift=np.fft.fftshift(np.fft.fft2(newimage_array))
print(inv)

f = plt.figure(constrained_layout=True)
gs = f.add_gridspec(1,2)

min=0
max=20
f_ax = f.add_subplot(gs[0,0])
im=f_ax.imshow(newimage_array, vmin=min, vmax=max,cmap='gray')

f_ax = f.add_subplot(gs[0,1])
im=f_ax.imshow(inv, cmap="gray")#, vmin=-5, vmax=5,cmap='gray')

f.subplots_adjust(right=0.8)

cbar_ax = f.add_axes([0.85, 0.15, 0.015, 0.7])
plt.suptitle("Stressed window Transmission and inverse FT")
plt.colorbar(im, cax=cbar_ax)
plt.show()
