import PIL as PIL
import matplotlib.pyplot as plt
import numpy as np
#%%
# Analysis of quantitative measurements
# Open images and check sizes

#damaged side of line window

im1 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\0.PNG')
im2 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\0H.PNG')
im3 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\1.PNG')
im4 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\1H.PNG')
im5 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\2.PNG')
im6 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\2H.PNG')
im7 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\3.PNG')
im8 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\3H.PNG')
im9 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\4.PNG')
im10 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\4H.PNG')
im11 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\5.PNG')
im12 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\5H.PNG')
im13 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\6.PNG')
im14 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\6H.PNG')
im15 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\7.PNG')
im16 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\7H.PNG')
im17 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\8.PNG')
im18 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\8H.PNG')
im19 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\9.PNG')
im20 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\9H.PNG')
im21 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\10.PNG')
im22 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\10H.PNG')
im23 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\11.PNG')

imB = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\Background.PNG')
images = [im1,im2,im3, im4, im5, im6, im7, im8, im9, im10,im11,im12,im13,im14,im15,im16,im17,im18,im19,im20, im21,im22,im23]
images2=[im1,im2,im3, im4, im5, im6, im7, im8, im9, im10]
imB_array =np.asarray(imB.convert('L'))
imB_array =imB_array.astype(np.int16)

f = plt.figure(constrained_layout=True)
gs = f.add_gridspec(4,6)
slicing=[600,850,750,1200]
im_height=slicing[1]-slicing[0]

slice_height=10
#analyses brightness through a thin slice
for i in range(len(images2)):
    im_array= np.asarray(images[i].convert('L'))
    im_array=im_array.astype(np.int16)
    newimage2_array=im_array-imB_array #background subtraction
    newimage2_array=newimage2_array[slicing[0]:slicing[1],slicing[2]:slicing[3]] #slice image to only contain the interesting part

    slice_start=int(0.5*im_height-0.5*slice_height) #take out a narrow slice
    slice_end=slice_start+slice_height
    slice=newimage2_array[slice_start:slice_end]

    avg_slice=(np.sum(slice,axis=0)/slice_height) #average over columns
    x=range(len(avg_slice))
    #plt.plot(x,avg_slice,label="image %s"%(i+1))#plot the intensities throughout the slice
    
    if i >=0 and i<6:
        f_ax = f.add_subplot(gs[0,i])
        im=f_ax.plot(x,avg_slice)
        #f.colorbar(im)
    elif i>= 6 and i<12:
        f_ax = f.add_subplot(gs[1, i-6])
        im=f_ax.plot(x,avg_slice)
        #f.colorbar(im)
    elif i>=12 and i<18:
        f_ax = f.add_subplot(gs[2, i-12])
        im=f_ax.plot(x,avg_slice)
        #f.colorbar(im)
    elif i>=18 and i<24:
        f_ax = f.add_subplot(gs[3, i-18])
        im=f_ax.plot(x,avg_slice)
        #f.colorbar(im)
        
#f.subplots_adjust(right=0.8)
#cbar_ax = f.add_axes([0.85, 0.15, 0.015, 0.7])
plt.suptitle("Lined window, damaged side, 0.5mm increments inwards")
#f.colorbar(im, cax=cbar_ax)
plt.legend()
plt.show()
