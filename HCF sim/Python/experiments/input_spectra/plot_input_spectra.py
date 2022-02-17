import matplotlib.pyplot as plt

#path to txt file
#import sys
#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\data\\HCF_scans\\power in\\")
f = open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\data\\HCF_scans\\power in\\Input_Power_Scan.txt', 'r')

content = f.read()
lines=[]
columns=[[],[],[],[],[],[],[],[],[],[],[]]
with open ('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\data\\HCF_scans\\power in\\Input_Power_Scan.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines.append(myline)

data=lines[22:] #gets rid of all the stuff at the top
for i in data:
    split=i.split("\t")
    for j in enumerate(split):
        columns[j].append(split[j])

#print(lines[:23])
print(columns[:10])

"""
wavel_nm=columns
print(wavel_nm)
intens1_2=columns[1]
print(intens1_2)
intens1_1=columns[2]
intens1_0=columns[3]
intens0_9=columns[4]
intens0_8=columns[5]
intens0_7=columns[6]
intens0_6=columns[7]
intens0_5=columns[8]
intens0_4=columns[9]
intens0_3=columns[10]
plt.plot(wavel_nm,intens1_2,label="1200mW")
plt.plot(wavel_nm,intens1_1,label="1100mW")
plt.plot(wavel_nm,intens1_0,label="1000mW")
plt.plot(wavel_nm,intens0_9,label="900mW")
plt.plot(wavel_nm,intens0_8,label="800mW")
plt.plot(wavel_nm,intens0_7,label="700mW")
plt.plot(wavel_nm,intens0_6,label="600mW")
plt.plot(wavel_nm,intens0_5,label="500mW")
plt.plot(wavel_nm,intens0_4,label="400mW")
plt.plot(wavel_nm,intens0_3,label="300mW")
plt.legend()
plt.xlabel("Wavelength, nm")
plt.ylabel("Intensity")
plt.show()
"""
f.close()
