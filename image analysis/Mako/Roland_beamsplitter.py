import PIL as PIL
import matplotlib.pyplot as plt
import numpy as np
#%%
# Analysis of quantitative measurements
# Open images and check sizes

#damaged side of Roland_beamsplitter_exp1000us window

im2 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\Roland_beamsplitter_exp1000us\\BS_1ND.PNG')
im3 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\Roland_beamsplitter_exp1000us\\BS_4ND.PNG')
im1 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\Roland_beamsplitter_exp1000us\\BS_noND.PNG')
im4 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\Roland_beamsplitter_exp1000us\\BS_5ND.PNG')


imB1 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\Roland_beamsplitter_exp1000us\\Background_noND.PNG')
imB2 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\Roland_beamsplitter_exp1000us\\Background_1ND.PNG')
imB3 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\Roland_beamsplitter_exp1000us\\Background_4ND.PNG')
imB4 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\Mako\\Roland_beamsplitter_exp1000us\\Background_5ND.PNG')

images = [im1,im2,im3,im4]


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
imB1_array =np.asarray(imB1.convert('L'))
imB1_array =imB1_array.astype(np.int16)

imB2_array =np.asarray(imB2.convert('L'))
imB2_array =imB2_array.astype(np.int16)

imB3_array =np.asarray(imB3.convert('L'))
imB3_array =imB3_array.astype(np.int16)

imB4_array =np.asarray(imB4.convert('L'))
imB4_array =imB4_array.astype(np.int16)

f = plt.figure(constrained_layout=True)
gs = f.add_gridspec(1,4)

im1_array= np.asarray(images[0].convert('L'))
im1_array=im1_array.astype(np.int16)
newimage1_array=im1_array-imB1_array

#newimage1_array=newimage1_array[800:1250,1000:1600]
max=50
min=-2
f_ax = f.add_subplot(gs[0,0])
im=f_ax.imshow(newimage1_array, vmin=min, vmax=max,cmap='gray')
        #f.colorbar(im)

im2_array= np.asarray(images[1].convert('L'))
im2_array=im2_array.astype(np.int16)
newimage2_array=im2_array-imB2_array

#newimage1_array=newimage1_array[800:1250,1000:1600]
f_ax = f.add_subplot(gs[0,1])
im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')

im3_array= np.asarray(images[2].convert('L'))
im3_array=im3_array.astype(np.int16)
newimage3_array=im3_array-imB3_array

#newimage1_array=newimage1_array[800:1250,1000:1600]
f_ax = f.add_subplot(gs[0,2])
im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')

im4_array= np.asarray(images[3].convert('L'))
im4_array=im4_array.astype(np.int16)
newimage4_array=im4_array-imB4_array

newimage4_array=newimage4_array[600:900,400:700]
f_ax = f.add_subplot(gs[0,3])
im=f_ax.imshow(newimage3_array, vmin=min, vmax=max,cmap='gray')

f.subplots_adjust(right=0.8)
cbar_ax = f.add_axes([0.85, 0.15, 0.015, 0.7])
plt.suptitle("Roland_beamsplitter_exp1000us window, 0.5mm increments inwards")
f.colorbar(im, cax=cbar_ax)
plt.show()

"""
for i in range(len(images)):
    im_array= np.asarray(images[i].convert('L'))
    im_array=im_array.astype(np.int16)
    newimage2_array=im_array-imsub_array

    newimage2_array=newimage2_array[800:1250,1000:1600]
    max=2
    min=-2
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
    elif i<30:
        f_ax = f.add_subplot(gs[4, i-24])
        im=f_ax.imshow(newimage2_array, vmin=min, vmax=max,cmap='gray')
        #f.colorbar(im)
f.subplots_adjust(right=0.8)
cbar_ax = f.add_axes([0.85, 0.15, 0.015, 0.7])
plt.suptitle("Roland_beamsplitter_exp1000us window, 0.5mm increments inwards")
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