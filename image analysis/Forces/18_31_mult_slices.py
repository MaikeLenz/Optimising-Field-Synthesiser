import PIL as PIL
import matplotlib.pyplot as plt
import numpy as np
#%%
# Analysis of quantitative measurements
# Open images and check sizes


im1 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\0.PNG')
im2 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\1.PNG')
im3 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\2.PNG')
im4 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\3.PNG')
im5 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\4.PNG')
im6 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\5.PNG')
im7 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\6.PNG')
im8 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\7.PNG')
im9 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\8.PNG')
im10 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\9.PNG')
im11 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\10.PNG')
im12 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\11.PNG')
im13 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\12.PNG')
im14 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\13.PNG')
im15 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\14.PNG')
im16 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\15.PNG')
im17 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\16.PNG')
im18 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\17.PNG')
im19 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\18.PNG')
im20 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\19.PNG')
im21 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\20.PNG')
im22= PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\21.PNG')
im23 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\22.PNG')
im24 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\23.PNG')
im25= PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\24.PNG')
im26 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\25.PNG')
im27 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\26.PNG')


imB = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Forces\\18_31ohms\\Background.PNG')
images = [im1,im2,im3, im4, im5, im6, im7, im8, im9, im10,im11,im12,im13,im14,im15,im16,im17,im18,im19,im20,im21,im22,im23,im24,im25,im26,im27]

imB_array =np.asarray(imB.convert('L'))
imB_array =imB_array.astype(np.int16)

imsub_array =np.asarray(imB.convert('L'))
imsub_array =imsub_array.astype(np.int16)
slicing=[600,1000,950,1400]

im_height=slicing[1]-slicing[0]

f = plt.figure(constrained_layout=True)
gs = f.add_gridspec(5,6)

heights=np.linspace(10,im_height-10,24)
slice_height=10

for i in range(len(heights)):
    im_array= np.asarray(images[13].convert('L'))
    im_array=im_array.astype(np.int16)
    newimage2_array=im_array-imsub_array
    newimage2_array=newimage2_array[slicing[0]:slicing[1],slicing[2]:slicing[3]]
    
    slice_start=int(heights[i]-0.5*slice_height) #take out a narrow slice
    slice_end=slice_start+slice_height
    slice=newimage2_array[slice_start:slice_end]

    avg_slice=(np.sum(slice,axis=0)/slice_height) #average over columns
    x=range(len(avg_slice))

    max=25
    min=-2
    if i >=0 and i<6:
        f_ax = f.add_subplot(gs[0,i])
        #im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        im=f_ax.plot(x,avg_slice)
    elif i>= 6 and i<12:
        f_ax = f.add_subplot(gs[1, i-6])
        #im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        im=f_ax.plot(x,avg_slice)
    elif i>=12 and i<18:
        f_ax = f.add_subplot(gs[2, i-12])
        #im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        im=f_ax.plot(x,avg_slice)
    elif i>=18 and i<24:
        f_ax = f.add_subplot(gs[3, i-18])
        #im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        im=f_ax.plot(x,avg_slice)
    elif i<30:
        f_ax = f.add_subplot(gs[4, i-24])
        #im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        im=f_ax.plot(x,avg_slice)
#f.subplots_adjust(right=0.8)
#cbar_ax = f.add_axes([0.85, 0.15, 0.015, 0.7])
plt.suptitle("Undamaged window, 18.3 Ohm")
#f.colorbar(im, cax=cbar_ax)
plt.show()
