from binascii import hexlify

def s8(value):
	return -(value & 0x80) | (value & 0x7f)

def process_header(header):
	'''
	A function which processes header in binary format and returns various header 
	information in appropriate format.

	Input: 
	------
	32-byte string in following sequence:
	MDRDSP(ID) = 8 bytes
	Source Name = 10 bytes
	Attenuator values = 4 bytes
	LO Frequency = 2 bytes
	FPGA Mon = 2 bytes
	GPS count = 2 bytes
	Packet count = 4 bytes

	Output:
	------
	Tuple of form (DSP_id, source_name, att_val, LO_freq, FPGA_Mon, GPSC, packet_count)
	'''
	DSP_id = header[:8].decode('ascii')
	source_name = header[8:18].decode('ascii')
	att_val = header[18:22]
	LO_freq = header[22:24]
	FPGA_Mon = header[24:26]
	GPSC = int(hexlify(header[26:28]), 16)
	packet_count = int(hexlify(header[28:]), 32)
	return (DSP_id, source_name, att_val, LO_freq, FPGA_Mon, GPSC, packet_count)

def process_data(packet):
	'''
	A fuction which processes body in binary format and returns X and Y polarization
	converted as 8-bit signed integer using 2's complement.

	Input:
	------
	1024-byte string. With alternate X and Y polarizations.

	Output:
	------
	Tuple of form (x_polarization, y_polarization)
	'''
	X = []
	Y = []
	for i in range(len(packet)):
		if i%2 == 0:
			X.append(s8(packet[i]))
		else:
			Y.append(s8(packet[i]))
	return X,Y


#Open files according to working tiles
fh1 = open('/home/dl/Projects/SWAN/Programs/SWAN-git/tile_data/VELA01', 'w')
# fh2 = open('/home/dl/Projects/SWAN/Programs/SWAN-git/tile_data/VELA02', 'w')
fh3 = open('/home/dl/Projects/SWAN/Programs/SWAN-git/tile_data/VELA03', 'w')
# fh4 = open('/home/dl/Projects/SWAN/Programs/SWAN-git/tile_data/VELA04', 'w')
fh5 = open('/home/dl/Projects/SWAN/Programs/SWAN-git/tile_data/VELA05', 'w')
fh6 = open('/home/dl/Projects/SWAN/Programs/SWAN-git/tile_data/VELA06', 'w')
fh7 = open('/home/dl/Projects/SWAN/Programs/SWAN-git/tile_data/VELA07', 'w')


x_pol = []
y_pol = []
path = path = '/home/dl/Projects/SWAN/Data/'
file_name = 'ch00_VELA_IISER_20190523_171203_000.mbr'
i = 0
with open(path + file_name, 'rb') as f:	#open resized1 file in read-binary format
	while True:
		i = i + 1
		header = f.read(32)
		body = f.read(1024)
		if len(header) < 32:
			break
		else:
			tile = process_header(header)[0][6:]
			processed_packet = process_data(body)
			# print(processed_packet)
			if tile == '01':
				for x, y in zip(processed_packet[0], processed_packet[1]) :
					fh1.write(str(x) + ' ' + str(y) + '\n')
			# if tile == '02':
			# 	for x, y in zip(processed_packet[0], processed_packet[1]) :
			# 		fh2.write(str(x) + ' ' + str(y) + '\n')
			if tile == '03':
				for x, y in zip(processed_packet[0], processed_packet[1]) :
					fh3.write(str(x) + ' ' + str(y) + '\n')
			# if tile == '04':
			# 	for x, y in zip(processed_packet[0], processed_packet[1]) :
			# 		fh4.write(str(x) + ' ' + str(y) + '\n')
			if tile == '05':
				for x, y in zip(processed_packet[0], processed_packet[1]) :
					fh5.write(str(x) + ' ' + str(y) + '\n')
			if tile == '06':
				for x, y in zip(processed_packet[0], processed_packet[1]) :
					fh6.write(str(x) + ' ' + str(y) + '\n')
			if tile == '07':
				for x, y in zip(processed_packet[0], processed_packet[1]) :
					fh7.write(str(x) + ' ' + str(y) + '\n')
		if i%10000 == 0: print("On packet number", i, 'out of 608430 packets.')
		if (i/6084.30)%10 == 0: print(i/6084.30, 'percent complete')
			
f.close()
fh1.close()
# fh2.close()
fh3.close()
# fh4.close()
fh5.close()
fh6.close()
fh7.close()

print('done!')