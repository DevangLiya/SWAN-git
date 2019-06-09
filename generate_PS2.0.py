#v2.0
#This version reads the mbr file and plots power spectrum.
#The spectrum is plotted without any cleaning of data.
#WARNING: The program might fill up the RAM and crash the system. It is recommended to have 
#         at least 8GB RAM. Do not run files larger than 500MB (tested limit).

#Immediate goals:
#Efficiency calculations to clean the data.
#Correct the axes.

import read_data as RD
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

#Read data and generate X, Y packets for FFT
# x_pol = []	#Toggle here for X
y_pol = []	#Toggle here for Y
file_path = '/home/dl/Projects/SWAN/Data/'
f_name = file_path + 'short'
print("Reading data....")
with open(f_name, 'rb') as f:	#open f_name in read-binary format
	while True:
		header = f.read(32)
		body = f.read(1024)
		if len(header) < 32:
			break
		else:
			processed_packet = RD.process_data(body)
			# x_pol.append(processed_packet[0])	#Toggle here for X
			y_pol.append(processed_packet[1])	#Toggle here for Y
f.close()

#FFT
print("Performing FFT....")
ffted = []
N = 512
for packet in y_pol:	#Change here for X/Y
	yr = fft(packet) 	#"raw" FFT with both + and - frequencies
	temp = pow(2/N * np.abs(yr[0:np.int(N/2)]), 2)	#positive frequencies only
	ffted.append(temp)

del y_pol	#Change here for X/Y

#Stacking function
def stacking(packets):
	'''
	A function which stacks given packets and returns a single packet.

	Input:
	------
	Array of shape n*m where n is number of packets and m is size of each packet.

	Output:
	------
	A single stacked numpy array.
	'''
	temp = np.zeros(len(packets[0]))	#Empty array of size m
	for packet in packets:
		temp = temp + packet
	return temp

#Stacking
print("Stacking the images....")
pulm_PS = []
for i in range(0, len(ffted), 60):
	pulm_PS.append(stacking(ffted[i:i+60])/60.0)
del ffted

pulm_PS2 = list(zip(*pulm_PS))	#Transpose
del pulm_PS

#Plotting
print("Generating the final image....")
plt.imshow(pulm_PS2, cmap=plt.cm.viridis, origin='lower')
plt.title("Power Spectrum of CasA (Y Polarization)")
plt.xlabel('Time (in s)')
plt.ylabel('Frequency (in Hz)')
plt.show()