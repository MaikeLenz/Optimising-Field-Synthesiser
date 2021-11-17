import PIL as PIL
import matplotlib.pyplot as plt
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

#%%
# Analysis of quantitative measurements
# Open images and check sizes

im1 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\chip_window\\Chip_0.PNG')
im2 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\chip_window\\Chip_1.PNG')
im3 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\chip_window\\Chip_2.PNG')
im4 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\chip_window\\Chip_3.PNG')
im5 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\chip_window\\Chip_4.PNG')
im6 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\chip_window\\Chip_5.PNG')
im7 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\chip_window\\Chip_6.PNG')
im8 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\chip_window\\Chip_7.PNG')
im9 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\chip_window\\Chip_8.PNG')
im10 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\chip_window\\Chip_9.PNG')
im11= PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\chip_window\\Chip_10.PNG')
im12= PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\chip_window\\Chip_11.PNG')
im13 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\chip_window\\Chip_12.PNG')

imB = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\chip_window\\Chip_Background.PNG')
images = [im1,im2,im3, im4, im5, im6, im7, im8, im9, im10,im11,im12,im13]

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

for image in images:
    newimage2_array=np.asarray(image.convert('L'))-np.asarray(imB.convert('L'))
    #newimage2=PIL.Image.fromarray(newimage2_array)
    #plt.figure()
    #plt.imshow(newimage2_array, cmap='gray')
    #plt.colorbar()
    if image == im1:
        print(newimage2_array[np.nonzero(newimage2_array)])

plt.figure()
plt.imshow(np.asarray(imB.convert('L')), cmap='gray')
plt.colorbar()

plt.show()