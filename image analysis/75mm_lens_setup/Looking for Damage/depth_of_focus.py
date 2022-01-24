import numpy as np
import matplotlib.pyplot as plt
import PIL as PIL

#wire images
front= PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\depth of focus\\front_wire_focus.png')
back = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\75mm_lens_setup\\depth of focus\\back_wire_unfocus.png')

images=[front,back]
f = plt.figure(constrained_layout=True)
gs = f.add_gridspec(1,2)

for i in range(len(images)):
    im_array= np.asarray(images[i].convert('L'))
    im_array=im_array.astype(np.int16)

    #newimage2_array=newimage2_array[600:850,750:1200]
    max=255
    min=-5
    if i >=0 and i<6:
        f_ax = f.add_subplot(gs[0,i])
        im=f_ax.imshow(im_array, vmin=min, vmax=max,cmap='gray')
        
f.subplots_adjust(right=0.8)
cbar_ax = f.add_axes([0.85, 0.15, 0.015, 0.7])
plt.suptitle("Front and back surface wires")
f.colorbar(im, cax=cbar_ax)
plt.show()