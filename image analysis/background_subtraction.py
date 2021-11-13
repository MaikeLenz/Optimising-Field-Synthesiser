import PIL as PIL
import matplotlib.pyplot as plt
import numpy as np
#%%
# Analysis of quantitative measurements
# Open images and check sizes

im1 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\split_window\\101121_0.PNG')
im2 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\split_window\\101121_1.PNG')
im3 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\split_window\\101121_2.PNG')
im4 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\split_window\\101121_3.PNG')
im5 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\split_window\\101121_4.PNG')
im6 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\split_window\\101121_5.PNG')
im7 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\split_window\\101121_6.PNG')
im8 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\split_window\\101121_7.PNG')
im9 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\split_window\\101121_8.PNG')
im10 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\split_window\\101121_9.PNG')
imB = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\split_window\\101121_Background1.PNG')
images = [im1,im2,im3, im4, im5, im6, im7, im8, im9, im10]

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
    newimage2_array=np.asarray(image)-np.asarray(imB)
    #newimage2=PIL.Image.fromarray(newimage2)
    plt.figure()
    plt.imshow(newimage2_array, interpolation='none')
    plt.colorbar()
plt.show()