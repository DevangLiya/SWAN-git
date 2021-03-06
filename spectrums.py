import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import pdb

#Open and read the file
path = '/home/dl/Projects/SWAN/Data/'
test_file_name = path + 'ch00_B0833-45_20150612_191438_010_4'
file_name = 'processed_data/' + 'VELA07'
print("Reading the data....")
fh = np.loadtxt(test_file_name, delimiter=' ', usecols=1) 
print("Data successfuly loaded. Preparing for FFT....")
# fh = fh1[:3584] #This was done to make len(fh)/512 an integer. Which is true for data
pulm_fft = np.array_split(fh, len(fh)/512)

#FFT
print("Performing FFT....")
ffted = []
N = 512
for packet in pulm_fft:
	yr = fft(packet) # "raw" FFT with both + and - frequencies
	temp = pow(2/N * np.abs(yr[0:np.int(N/2)]), 2) # positive frequencies only
	ffted.append(temp)

#Stacking function
def stacking(packets):
	temp = np.zeros(len(packets[0]))
	for packet in packets:
		temp = temp + packet
	return temp

#Stacking
print("Stacking the images....")
pulm_PS = np.array([stacking(ffted[:60])/60.0])	#List of 256-length arrays
for i in range(60, len(ffted), 60):
	pulm_PS = np.vstack((pulm_PS, stacking(ffted[i:i+60])/60.0))


#Convert to channel-wise array
pulm_PS2 = pulm_PS.T 

#Compare power spectrums (Cluttered code here)
# plt.plot(pow(pulm_PS[0],2), color='blue', label='Stacked (60)')
# for i in range(60):
# 	plt.plot(pow(ffted[i], 2), color='red', alpha=0.2)
# plt.plot(pow(ffted[0],2), color='red', label='Single Packet')
# for i in range(940, len(pulm_PS)):
# 	plt.plot(pow(pulm_PS[i], 2), color='blue')
# 	plt.xlabel('Spectral Channel')
# 	plt.ylabel('Intensity')
# 	plt.title('Stacked power spectrum ' + str(i) + ' (Vela pulsar)')
# 	image_name = '/home/dl/Projects/SWAN/Programs/stacked/image' + str(i) + '.png'
# 	plt.savefig(image_name, dpi=500)
# 	plt.clf()
# plt.legend(loc='upper right')
# plt.show()

#Plot dynamic spectrum
print("Generating the dynamic spectrum....")
plt.imshow(pulm_PS2, cmap=plt.cm.viridis, origin='lower')
plt.title("Dynamic Spectrum of Vela pulsar")
plt.xlabel('Time (10^-3 s)')
plt.ylabel('Frequency Channel')
plt.show()

pdb.set_trace()
