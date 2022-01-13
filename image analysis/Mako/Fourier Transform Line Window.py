# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 11:21:35 2022

@author: iammo
"""

import PIL as PIL
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy.fft import ifft2
#%%
# Analysis of quantitative measurements
# Open images and check sizes

#damaged side of line window

im1 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\0.PNG')
im2 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\0H.PNG')
im3 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\1.PNG')
im4 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\1H.PNG')
im5 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\2.PNG')
im6 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\2H.PNG')
im7 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\3.PNG')
im8 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\3H.PNG')
im9 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\4.PNG')
im10 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\4H.PNG')
im11 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\5.PNG')
im12 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\5H.PNG')
im13 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\6.PNG')
im14 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\6H.PNG')
im15 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\7.PNG')
im16 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\7H.PNG')
im17 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\8.PNG')
im18 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\8H.PNG')
im19 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\9.PNG')
im20 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\9H.PNG')
im21 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\10.PNG')
im22 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\10H.PNG')
im23 = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\11.PNG')

imB = PIL.Image.open(r'D:\MSci\Imaging Damage\Damaged Windows\Mako Camera\Line\Background.PNG')
images = [im1,im2,im3, im4, im5, im6, im7, im8, im9, im10,im11,im12,im13,im14,im15,im16,im17,im18,im19,im20, im21,im22,im23]

imB_array =np.asarray(imB.convert('L'))
imB_array =imB_array.astype(np.int16)

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
#%%
# Fourier Transform Images
im_array= np.asarray(images[3].convert('L'))
im_array=im_array.astype(np.int16)
newimage2_array=im_array-imB_array
newimage2_array=newimage2_array[600:850,750:1200]
newimageFT = ifft2(newimage2_array)

newimageFT_real = []
for i in range(len(newimageFT)):
    row = []
    for j in range(len(newimageFT[i])):
        row.append(newimageFT[i][j].real)
    newimageFT_real.append(row)
#print(newimageFT)

maximum=0.05
minimum=-0.05
plt.figure()
plt.imshow(newimageFT_real, cmap='gray', vmin=minimum, vmax=maximum)
plt.colorbar()

#print(newimageFT_real)

newimageFT_im = []
for i in range(len(newimageFT)):
    row = []
    for j in range(len(newimageFT[i])):
        row.append(newimageFT[i][j].imag)
    newimageFT_im.append(row)
    
#print(newimageFT_im)
plt.figure()
plt.imshow(newimageFT_im, cmap='gray', vmin=minimum, vmax=maximum)
#%%
# Try shifting to center - center at roughly 220 pixels horizontally and 140 pixels vertically


newimageFT_shift = fftshift(newimageFT)
print(newimageFT_shift)

newimageFT_real_shift = []
for i in range(len(newimageFT_shift)):
    row = []
    for j in range(len(newimageFT_shift[i])):
        row.append(newimageFT_shift[i][j].real)
    newimageFT_real_shift.append(row)
#print(newimageFT)

maximum=1
minimum=0
plt.figure()
plt.imshow(newimageFT_real_shift, cmap='gray', vmin=minimum, vmax=maximum)
plt.colorbar()

#print(newimageFT_real)

newimageFT_im_shift = []
for i in range(len(newimageFT_shift)):
    row = []
    for j in range(len(newimageFT_shift[i])):
        row.append(newimageFT_shift[i][j].imag)
    newimageFT_im_shift.append(row)
    
#print(newimageFT_im)
plt.figure()
plt.imshow(newimageFT_im_shift, cmap='gray', vmin=minimum, vmax=maximum)

