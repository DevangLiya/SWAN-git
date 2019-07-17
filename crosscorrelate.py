import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import pdb

#Open and read the file
path = '/home/dl/Projects/SWAN/Data/'
test_file_name = path + 'fft_test'
file_name = 'processed_data/' + 'VELA07'
print("Reading the data....")
x_pol = np.loadtxt(file_name, delimiter=' ', usecols=0)
print("First column loaded. Loading second column....")
y_pol = np.loadtxt(file_name, delimiter=' ', usecols=1)
print("Data successfuly loaded. Preparing for FFT....")
pulm_fft_x = np.array_split(x_pol, len(x_pol)/512)
pulm_fft_y = np.array_split(y_pol, len(y_pol)/512)
print(len(pulm_fft_y), len(pulm_fft_x))


#FFT
print("Performing FFT....")
ffted = []
# ffted_single = []
# residue = []
N = 512
for x, y in zip(pulm_fft_x, pulm_fft_y):
	yr_x = fft(x) # "raw" FFT with both + and - frequencies
	yr_y = fft(y) # "raw" FFT with both + and - frequencies
	ffted.append(np.real(yr_x[0:np.int(N/2)]*(yr_y[0:np.int(N/2)].conj())))
	# residue.append(np.imag(yr_x[0:np.int(N/2)]*(yr_y[0:np.int(N/2)].conj())))
	# ffted_single.append(np.abs(yr_y[0:np.int(N/2)]))

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
pulm_PS2[0] = 0

#Plot dynamic spectrum
print("Generating the dynamic spectrum....")
plt.imshow(pulm_PS2, cmap=plt.cm.viridis, origin='lower')
plt.title("Cross Spectrum of vela")
plt.xlabel('Time (10^-3 s)')
plt.ylabel('Frequency Channel')
plt.show()

pdb.set_trace()
