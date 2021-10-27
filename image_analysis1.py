# First must pip install Pillow
import matplotlib
import PIL.Image

# Open images and check sizes
im1 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\DamageStart.PNG')
print(im1.format, im1.size, im1.mode)
im2 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\DamageMiddle.PNG')
#print(im2.format, im2.size, im2.mode)
im3 = PIL.Image.open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\images\\DamageEnd.PNG')
#print(im3.format, im3.size, im3.mode)

# Crop to all the same size
box = (0, 0, 900, 520)
p1 = im1.crop(box)
p2 = im2.crop(box)
p3 = im3.crop(box)
#print(p1.size)

# Convert to black and white
p1 = p1.convert('L')
p2 = p2.convert('L')
p3 = p3.convert('L')
#print(p1.mode)

# Get pixel values- note: smaller=darker, 0-255
pixel_values1 = list(p1.getdata())
pixel_values2 = list(p2.getdata())
pixel_values3 = list(p3.getdata())
#print(pixel_values1)

# Choose some cutoff for brightness
cutoff = 200

# Count number of pixels above cutoff
counter1 = 0
for i in pixel_values1:
    if i > cutoff:
        counter1 += 1
counter2 = 0
for i in pixel_values2:
    if i > cutoff:
        counter2 += 1
counter3 = 0
for i in pixel_values3:
    if i > cutoff:
        counter3 += 1
       
print(counter1)
print(counter2)
print(counter3)