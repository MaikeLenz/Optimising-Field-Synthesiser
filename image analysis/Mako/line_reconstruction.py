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

img1 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\glue\\0.PNG')
img2 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\glue\\1.PNG')
img3 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\glue\\2.PNG')
img4 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\glue\\3.PNG')
img5 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\glue\\4.PNG')
img6 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\glue\\5.PNG')
img7 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\glue\\6.PNG')
img8 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\glue\\7.PNG')
img9 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\glue\\8.PNG')
img10 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\glue\\9.PNG')
img11 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\glue\\10.PNG')

imB = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\line\\Background.PNG')
imgB = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\glue\\Background.PNG')

images = [im1,im2,im3, im4, im5, im6, im7, im8, im9, im10,im11,im12,im13,im14,im15,im16,im17,im18,im19,im20, im21,im22,im23]
glue_images = [img1,img2,img3,img4,img5,img6, img7, img8,img9,img10,img11,imgB]

window_width_mm=50
px_size_mm=0.0022
mag=13.5
shift=1/(mag*px_size_mm)

imB_array =np.asarray(imB.convert('L'))
imB_array =imB_array.astype(np.int16)

imgB_array =np.asarray(imgB.convert('L'))
imgB_array =imgB_array.astype(np.int16)

"""
for i in range(len(test)):
    for j in test[i]:
        if test[i][j] >200:
            test[i][j]=0
print(test)

"""
"""
for image in images:
    newimage = PIL.ImageChops.subtract(image, im5)

    mask1 = PIL.Image.eval(newimage, lambda a: 0) #if a <= 24 else 255)
    mask2 = mask1.convert('1')

    blank = PIL.Image.eval(newimage, lambda a: 0)

    new = PIL.Image.composite(newimage, blank, mask2) 

    #diff= PIL.ImageChops.difference(image, imB)

    plt.figure()
    plt.imshow(np.asarray(new), interpolation='nearest', cmap="gray")
    #plt.imshow(np.asarray(diff), interpolation='nearest', cmap="gray")

    plt.colorbar()
plt.show()
"""
"""

f = plt.figure(constrained_layout=True)
gs = f.add_gridspec(4,6)

for i in range(len(images)):
    im_array= np.asarray(images[i].convert('L'))
    im_array=im_array.astype(np.int16)
    newimage2_array=im_array-imB_array

    newimage2_array=newimage2_array[600:850,750:1200]
    max=20
    min=-5
    if i >=0 and i<6:
        f_ax = f.add_subplot(gs[0,i])
        im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        #f.colorbar(im)
    elif i>= 6 and i<12:
        f_ax = f.add_subplot(gs[1, i-6])
        im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        #f.colorbar(im)
    elif i>=12 and i<18:
        f_ax = f.add_subplot(gs[2, i-12])
        im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        #f.colorbar(im)
    elif i>=18 and i<24:
        f_ax = f.add_subplot(gs[3, i-18])
        im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        #f.colorbar(im)
f.subplots_adjust(right=0.8)
cbar_ax = f.add_axes([0.85, 0.15, 0.015, 0.7])
plt.suptitle("Lined window, damaged side, 0.5mm increments inwards")
f.colorbar(im, cax=cbar_ax)
plt.show()
"""
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

plt.figure()
#print(int((window_width_mm/mag)/px_size_mm))
empty_image=np.zeros((250,int((window_width_mm/mag)/px_size_mm)))
final_image=np.zeros((250,int((window_width_mm/mag)/px_size_mm)))

#print(len(empty_image),len(empty_image[0]))
plt.imshow(empty_image)
slicing=[600,850,750,1200]
im_width=slicing[3]-slicing[2]
im_height= slicing[1]-slicing[0]
slice_height=4

#add up elements in array
for i in range(len(images)):
    im_array= np.asarray(images[i].convert('L'))
    im_array=im_array.astype(np.int16)
    newimage2_array=im_array-imB_array
    newimage2_array=newimage2_array[slicing[0]:slicing[1],slicing[2]:slicing[3]]
    px_start=int(i*shift)#
    whole_image = np.append(empty_image[:,:px_start],newimage2_array, axis=1)
    whole_image2=np.append(whole_image,empty_image[:,px_start+im_width:], axis=1)
    out_array=np.add(final_image,whole_image2)
    final_image=out_array

for i in range(len(glue_images)):
    img_array= np.asarray(glue_images[i].convert('L'))
    img_array=img_array.astype(np.int16)
    newimage2_array=img_array-imgB_array
    #glue reconstruction:newimage2_array=newimage2_array[600:1000,900:1300]
    newimage2_array=newimage2_array[600:850,900:1350]   
    px_start=len(empty_image[0])-int(i*shift)-im_width
    whole_image = np.append(empty_image[:,:px_start],newimage2_array, axis=1)
    whole_image2=np.append(whole_image,empty_image[:,px_start+im_width:], axis=1)
    out_array=np.add(final_image,whole_image2)
    final_image=out_array

plt.imshow(final_image, cmap='gray')
plt.show()

slice_start=int(0.5*im_height-0.5*slice_height) #take out a narrow slice
slice_end=slice_start+slice_height
slice=final_image[slice_start:slice_end]

avg_slice=(np.sum(slice,axis=0)/slice_height) #average over columns
x=range(len(avg_slice))
plt.plot(x,avg_slice)#plot the intensities throughout the slice
"""
#overlay images
for i in range(len(images)):
    im_array= np.asarray(images[i].convert('L'))
    im_array=im_array.astype(np.int16)
    newimage2_array=im_array-imB_array
    newimage2_array=newimage2_array[slicing[0]:slicing[1],slicing[2]:slicing[3]]
    px_start=int(i*shift)#
    whole_image = np.append(empty_image[:,:px_start-1],newimage2_array, axis=1)
    whole_image2=np.append(whole_image,empty_image[:,px_start-1+im_width:], axis=1)
    #print(len(whole_image2), len(whole_image2[0]))
    #print(newimage2_array.shape[0])
    #whole_image2 = np.append(whole_image,empty_image[:,px_start-1+len(newimage2_array[0]):],axis=1)
    plt.imshow(whole_image, cmap='gray', alpha=0.15)

for i in range(len(glue_images)):
    img_array= np.asarray(glue_images[i].convert('L'))
    img_array=img_array.astype(np.int16)
    newimage2_array=img_array-imgB_array
    #glue reconstruction:newimage2_array=newimage2_array[600:1000,900:1300]
    newimage2_array=newimage2_array[600:850,900:1350]   
    px_start=len(empty_image[0])-int(i*shift)-im_width
    #whole_image = np.append(empty_image[:,:px_start-1],newimage2_array, axis=1)
    #print(len(whole_image[0]))
    #print(newimage2_array.shape[0])
    #whole_image2 = np.append(whole_image,empty_image[:,px_start-1+len(newimage2_array[0]):],axis=1)
    plt.imshow(newimage2_array, cmap='gray', alpha=0.15, extent=(px_start,px_start+im_width,0,250))
"""

plt.show()

#plt.imshow(empty_image[:,:100])
#plt.show()