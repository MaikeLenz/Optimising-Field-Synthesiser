# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:58:02 2022

@author: iammo
"""

import PIL as PIL
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
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
images2=[im1, im2, im3, im4, im5, im6, im7, im8, im9, im10]
imB_array =np.asarray(imB.convert('L'))
imB_array =imB_array.astype(np.int16)

f = plt.figure(constrained_layout=True)
gs = f.add_gridspec(2,4)
slicing=[600,850,750,1200]
im_height=slicing[1]-slicing[0]

slice_height=10
def Gauss(x, A, u, o):
    return A*np.exp(-((x-u)**2)/(2*(o**2)))
def two_Gauss(x, A1,A2, u1,u2, o1,o2):
    return A1*np.exp(-((x-u1)**2)/(2*(o1**2)))+A2*np.exp(-((x-u2)**2)/(2*(o2**2)))

big_pos=[]
big_pos_err=[]
small_pos=[]
small_pos_err=[]
fitted_params = []
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
    x_pixels=range(len(avg_slice))
    x=[]
    for j in x_pixels:
        x.append(j*2.2*7.815/(10**3))
    #plt.plot(x,avg_slice,label="image %s"%(i+1))#plot the intensities throughout the slice
    # curve fit
    """
    if i==0:
        popt, _ = curve_fit(two_Gauss, x, avg_slice,p0=[5,5,310,310,50,50])
    elif i==1:
        popt, _ = curve_fit(two_Gauss, x, avg_slice,p0=[5,5,310,310,50,50])
    elif i==2:
        popt, _ = curve_fit(two_Gauss, x, avg_slice,p0=[12,5,310,250,50,50])
    elif i==3:
        popt, _ = curve_fit(two_Gauss, x, avg_slice,p0=[12,5,310,250,50,50])
    elif i==4:
        popt, _ = curve_fit(two_Gauss, x, avg_slice,p0=[10,6,300,250,20,50])
    elif i<6:
        popt, _ = curve_fit(two_Gauss, x, avg_slice,p0=[6,5,300,300,50,50])
    elif i>6:
        popt, _ = curve_fit(two_Gauss, x, avg_slice,p0=[12,5,200,300,50,50])
    else:
        popt, _ = curve_fit(two_Gauss, x, avg_slice,p0=[12,5,210,290,30,50])
    print(popt)
    # summarize the parameter values
    A1,A2, u1,u2, o1,o2 = popt 
    big_pos.append(u1)
    small_pos.append(u2) 
    """
    
    if i==0:
        #popt, _ = curve_fit(two_Gauss, x, avg_slice,p0=[5,5,9.37,9.37,2,2])
        popt = [0,0,0,0,0,0]
    elif i==1:
        #popt, _ = curve_fit(two_Gauss, x, avg_slice,p0=[5,5,9.37,9.37,2,2])
        popt = [0,0,0,0,0,0]
    elif i==2:
        popt, cov = curve_fit(two_Gauss, x, avg_slice,p0=[10,4,5.4,4.4,0.37,0.17], bounds=(0, np.inf))
    elif i==3:
        popt, cov = curve_fit(two_Gauss, x, avg_slice,p0=[13,5,5.28,4.34,1.37,1.17], bounds=(0, np.inf))
    elif i==4:
        popt, cov = curve_fit(two_Gauss, x, avg_slice,p0=[12,4,5.05,4.34,1.37,1.17], bounds=(0, np.inf))
    elif i==5:
        popt, cov = curve_fit(two_Gauss, x, avg_slice,p0=[10,4,4.4,5.64,0.59,0.23], bounds=(0, np.inf))
    elif i==6:
        popt, cov = curve_fit(two_Gauss, x, avg_slice,p0=[12,6,4,5.22,0.5,0.12], bounds=(0, np.inf))
    elif i==7:
        popt, cov = curve_fit(two_Gauss, x, avg_slice,p0=[13,7,3.8,5.1,0.5,0.3], bounds=(0, np.inf))
    elif i==8:
        popt, cov = curve_fit(two_Gauss, x, avg_slice,p0=[13,5,3.87,4.93,0.92,0.92], bounds=(0, np.inf))
    elif i==9:
        popt, cov = curve_fit(two_Gauss, x, avg_slice,p0=[10,6,4.11,5.28,0.22,0.22], bounds=(0, np.inf))
    else:
        popt, cov = curve_fit(two_Gauss, x, avg_slice,p0=[10,6,210,290,30,50])
    #print(popt)
    # summarize the parameter values
    A1,A2, u1,u2, o1,o2 = popt 
    big_pos.append(u1)
    small_pos.append(u2)
    fitted_params.append(popt)
    if i>=2:
        big_pos_err.append(cov[2,2])
        small_pos_err.append(cov[3,3])
    
    if i==0 or i==1:
        pass
    elif i >=2 and i<6:
        f_ax = f.add_subplot(gs[0,i-2])
        im=f_ax.plot(x,avg_slice) 
        plt.plot(x,Gauss(x,popt[0],popt[2],popt[4]))  
        plt.plot(x,Gauss(x,popt[1],popt[3],popt[5]))
    elif i>= 6 and i<10:
        f_ax = f.add_subplot(gs[1, i-7])
        im=f_ax.plot(x,avg_slice)
        plt.plot(x,Gauss(x,popt[0],popt[2],popt[4]))  
        plt.plot(x,Gauss(x,popt[1],popt[3],popt[5]))   
    """
    elif i>=10 and i<15:
        f_ax = f.add_subplot(gs[2, i-10])
        im=f_ax.plot(x,avg_slice)
        plt.plot(x,Gauss(x,popt[0],popt[2],popt[4]))  
        plt.plot(x,Gauss(x,popt[1],popt[3],popt[5]))         
    elif i>=15 and i<20:
        f_ax = f.add_subplot(gs[3, i-15])
        im=f_ax.plot(x,avg_slice)
        plt.plot(x,Gauss(x,popt[0],popt[2],popt[4]))  
        plt.plot(x,Gauss(x,popt[1],popt[3],popt[5]))  
    """
    """    
    plt.figure()
    plt.plot(x,avg_slice)
    plt.plot(x,Gauss(x,popt[0],popt[2],popt[4]))  
    plt.plot(x,Gauss(x,popt[1],popt[3],popt[5]))  
    """
big_steps=[]
small_steps=[]

for i in range(len(big_pos)-1):
    big_steps.append(big_pos[i+1]-big_pos[i])
    small_steps.append(small_pos[i+1]-small_pos[i])

#print(big_steps)
#print(small_steps)
#f.subplots_adjust(right=0.8)
#cbar_ax = f.add_axes([0.85, 0.15, 0.015, 0.7])
plt.suptitle("Damaged Window with 0.5mm Increments between Images", fontsize=18)
f.text(0.5, 0.04, 'Distance along Window (mm)', ha='center', fontsize=12)
f.text(0.02, 0.5, 'Relative Intensity', va='center', rotation='vertical', fontsize=12)
#f.colorbar(im, cax=cbar_ax)
#plt.legend()
plt.show()

mag_percentage_err = 0.2938/7.815
big_err=[]
for i in range(len(big_pos_err)):
    big_err.append(mag_percentage_err*big_pos[i+2] + 1.1*0.001 + 0.2 + big_pos_err[i])
small_err=[]
for i in range(len(small_pos_err)):
    small_err.append(mag_percentage_err*small_pos[i+2] + 1.1*0.001 + 0.2 + small_pos_err[i])

# Plotting movement
def line(x, m, c):
    return m*x + c

popt, cov = curve_fit(line, range(len(images2)-2), big_pos[2:])
plt.figure()
plt.errorbar(range(len(images2)-2), big_pos[2:], yerr=big_err, color='tab:orange', label='Large Peak')
plt.errorbar(range(len(images2)-2), small_pos[2:], yerr=small_err, color='tab:green', label='Small Peak')
plt.plot(range(len(images2)-2), line(range(len(images2)-2), popt[0], popt[1]), color='black', label='Linear Fit')
plt.legend()
plt.xlabel('Image Number', fontsize=12)
plt.ylabel('Peak Position (mm)', fontsize=12)
plt.title('The Positions of the Peaks Determined from Gaussian Fits', fontsize=18)

#%%
# Try subtracting the large peak from each image
f = plt.figure(constrained_layout=True)
gs = f.add_gridspec(2,4)

means = []
for i in range(len(images2)):
    im_array= np.asarray(images[i].convert('L'))
    im_array=im_array.astype(np.int16)
    newimage2_array=im_array-imB_array #background subtraction
    newimage2_array=newimage2_array[slicing[0]:slicing[1],slicing[2]:slicing[3]] #slice image to only contain the interesting part

    slice_start=int(0.5*im_height-0.5*slice_height) #take out a narrow slice
    slice_end=slice_start+slice_height
    slice=newimage2_array[slice_start:slice_end]

    avg_slice=(np.sum(slice,axis=0)/slice_height) #average over columns
    x_pixels=range(len(avg_slice))
    x=[]
    for j in x_pixels:
        x.append(j*2.2*7.815/(10**3))
    single_peak = []

    if i != 0 and i != 1:
        for j in range(len(avg_slice)):
            single_peak.append(avg_slice[j] - Gauss(x[j], fitted_params[i][0], fitted_params[i][2], fitted_params[i][4]))
        popt, cov = curve_fit(Gauss, x, single_peak, p0=[5,5,1])
        means.append(popt[1])
    if i==0 or i==1:
        pass
    elif i >=2 and i<6:
        f_ax = f.add_subplot(gs[0,i-2])
        im=f_ax.plot(x,single_peak) 
        plt.plot(x,Gauss(x,*popt), color='tab:green')  
    elif i>= 6 and i<10:
        f_ax = f.add_subplot(gs[1, i-7])
        im=f_ax.plot(x,single_peak)
        plt.plot(x,Gauss(x,*popt), color='tab:green')
plt.suptitle("Damaged Window with the Large Peak Subtracted", fontsize=18)
f.text(0.5, 0.04, 'Distance along Window (mm)', ha='center', fontsize=12)
f.text(0.02, 0.5, 'Relative Intensity', va='center', rotation='vertical', fontsize=12)

plt.figure()
plt.plot(range(len(images2)-2), means, color='tab:green')
plt.xlabel('Image Number', fontsize=12)
plt.ylabel('Peak Position (mm)', fontsize=12)
plt.title('The Positions of the Smaller Peaks Determined from Gaussian Fits', fontsize=18)
