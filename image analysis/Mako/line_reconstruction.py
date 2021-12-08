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

window_width_mm= 42.77
px_size_mm=0.0022
mag=13.5

def mm_to_px(mm):
    return int(mm/(mag*px_size_mm))

shift=mm_to_px(1)

imB_array =np.asarray(imB.convert('L'))
imB_array =imB_array.astype(np.int16)

imgB_array =np.asarray(imgB.convert('L'))
imgB_array =imgB_array.astype(np.int16)


plt.figure()
#print(int((window_width_mm/mag)/px_size_mm))
empty_image=np.zeros((250,mm_to_px(window_width_mm)))
final_image=np.zeros((250,mm_to_px(window_width_mm)))

#print(len(empty_image),len(empty_image[0]))
plt.imshow(empty_image)
slicing=[600,850,750,1200]
im_width=slicing[3]-slicing[2]
im_height= slicing[1]-slicing[0]
slice_height=4
start_posn_mm=0.6 #how many mm into the window the centre of the first image is

left_offset= int(0.5*im_width - mm_to_px(start_posn_mm))    

def cut_image(image_array,px_start):
    if px_start<0:
        image_array=image_array[:,abs(px_start):]
        return image_array, 0 
    elif px_start>(len(empty_image[0])-im_width):
        image_array=image_array[:,:(px_start-(len(empty_image[0])-im_width))]
        return image_array, px_start
    else:
        return image_array, px_start


#add up elements in array
for i in range(len(images)):
    im_array= np.asarray(images[i].convert('L'))
    im_array=im_array.astype(np.int16)
    newimage2_array=im_array-imB_array
    newimage2_array=newimage2_array[slicing[0]:slicing[1],slicing[2]:slicing[3]]
    px_start=int(i*shift)-left_offset
    newimage2_array,px_start = cut_image(newimage2_array,px_start)

    whole_image = np.append(empty_image[:,:px_start],newimage2_array, axis=1)
    whole_image2=np.append(whole_image,empty_image[:,px_start+len(newimage2_array[0]):], axis=1)
    final_image=np.add(final_image,whole_image2)

for i in range(len(glue_images)):
    img_array= np.asarray(glue_images[i].convert('L'))
    img_array=img_array.astype(np.int16)
    newimage2_array=img_array-imgB_array
    #glue reconstruction:newimage2_array=newimage2_array[600:1000,900:1300]
    newimage2_array=newimage2_array[600:850,900:1350] 
    px_start=len(empty_image[0])+left_offset-int(i*shift)-im_width
    print(px_start)
    newimage2_array,px_start = cut_image(newimage2_array,px_start)

    whole_image = np.append(empty_image[:,:px_start],newimage2_array, axis=1)
    whole_image2=np.append(whole_image,empty_image[:,(px_start+len(newimage2_array[0])):], axis=1)
    final_image=np.add(final_image,whole_image2)


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
