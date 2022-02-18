import matplotlib.pyplot as plt

#path to txt file
lines=[]
columns=[[],[],[],[],[],[],[],[],[],[],[]]
with open ('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\data\\HCF_scans\\power in\\Input_Power_Scan.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines.append(myline)

data=lines[22:] #gets rid of all the stuff at the top
for i in data:
    split=i.split("\t") #delimiter is \t
    for j ,value in enumerate(split):
        columns[j].append(float(value))

wavel_nm=np.array(columns[0])
intens1_2=np.array(columns[1])
intens1_1=np.array(columns[2])
intens1_0=np.array(columns[3])
intens0_9=np.array(columns[4])
intens0_8=np.array(columns[5])
intens0_7=np.array(columns[6])
intens0_6=np.array(columns[7])
intens0_5=np.array(columns[8])
intens0_4=np.array(columns[9])
intens0_3=np.array(columns[10])
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

