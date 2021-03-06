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
images = [im1,im2,im3, im4, im5, im6, im7, im8, im9, im10, imB]
#for i in images:
#    print(i.format, i.size, i.mode)


#box = (0, 0, 1200, 500)

#im3 = im3.crop(box)
im3 = im3.convert('L')
#im4 = im4.crop(box)
im4 = im4.convert('L')
#im5 = im5.crop(box)
im5 = im5.convert('L')
#im6 = im6.crop(box)
im6 = im6.convert('L')
#im7 = im7.crop(box)
im7 = im7.convert('L')
#im8 = im8.crop(box)
im8 = im8.convert('L')
#im9 = im9.crop(box)
im9 = im9.convert('L')
#im10 = im10.crop(box)
im10 = im10.convert('L')
#im1 = im1.crop(box)
im1 = im1.convert('L')
#im2 = im2.crop(box)
im2 = im2.convert('L')
#imB = imB.crop(box)
imB = imB.convert('L')


im3 = np.array(im3)
im4 = np.array(im4)
im5 = np.array(im5)
im6 = np.array(im6)
im7 = np.array(im7)
im8 = np.array(im8)
im9 = np.array(im9)
im10 = np.array(im10)
im1 = np.array(im1)
im2 = np.array(im2)
imB = np.array(imB)
images = [im1, im2, im3, im4, im5, im6, im7, im8, im9, im10, imB]



"""
pixel_values3 = list(im3.getdata())
pixel_values4 = list(im4.getdata())
pixel_values5 = list(im5.getdata())
pixel_values6 = list(im6.getdata())
pixel_values7 = list(im7.getdata())
pixel_values8 = list(im8.getdata())
pixel_values9 = list(im9.getdata())
pixel_values10 = list(im10.getdata())
pixel_values11 = list(im11.getdata())
pixel_values12 = list(im12.getdata())
pixel_values13 = list(im13.getdata())
pixel_valuesB = list(imB.getdata())

totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in pixel_values3:
    totals[0] += i
for i in pixel_values4:
    totals[1] += i
for i in pixel_values5:
    totals[2] += i
for i in pixel_values6:
    totals[3] += i
for i in pixel_values7:
    totals[4] += i
for i in pixel_values8:
    totals[5] += i
for i in pixel_values9:
    totals[6] += i
for i in pixel_values10:
    totals[7] += i
for i in pixel_values11:
    totals[8] += i
for i in pixel_values12:
    totals[9] += i
for i in pixel_values13:
    totals[10] += i
for i in pixel_valuesB:
    totals[11] += i
   
print(totals)

"""
#%%
""""
number = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
plt.plot(number, totals[:-1])
#%%
# Minus the background from all
pixel_values = [pixel_values3, pixel_values4, pixel_values5, pixel_values6, pixel_values7, pixel_values8, pixel_values9, pixel_values10, pixel_values11, pixel_values12, pixel_values13]
new_pixel_values = []
for i in pixel_values:
    new_pixel_values.append(np.array(np.array(i) - np.array(pixel_valuesB)))
"""
"""
totals = np.zeros(11)
for i in range(len(new_pixel_values)):
    for j in new_pixel_values[i]:
        totals[i] += j
#%%        
cutoff = 0
intensity = np.zeros(11)
for i in range(len(new_pixel_values)):
    for j in new_pixel_values[i]:
        if j > cutoff:
            intensity[i] += j
           
#plt.plot(number, intensity)
"""
#%%
imB_array=np.asarray(imB)
#imB_array = PIL.Image.fromarray(np.array(imB))
for image in images:
    newimage=np.asarray(image)
    newimag=np.zeros((len(newimage),len(newimage[0])))
    #newimage = PIL.Image.fromarray(np.array(images[i]))
    for i in range(len(newimage)):
        for j in range(len(newimage[i])):
    #images[i].setflags(write=1)
            newimag[i][j]=newimage[i][j]-imB_array[i][j]
    plt.figure()
    #plt.imshow(newimage, interpolation='nearest', cmap='gray')
    plt.imshow(np.array(newimag), interpolation='none')
    plt.colorbar()
plt.show()