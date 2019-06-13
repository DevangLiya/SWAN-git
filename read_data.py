from binascii import hexlify

def s8(value):
	'''
	A function to take 8-bit 2's complement

	Input:
	------
	8-bit binary string

	Output:
	------
	An integer between -128 and 127
	'''
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


if __name__ == "__main__":
	headers = []
	x_pol = []
	y_pol = []
	path = 'raw_data/'
	file_name = 'resized1_296'
	with open(path + file_name, 'rb') as f:	#open file in read-binary format
		while True:
			header = f.read(32)
			body = f.read(1024)
			if len(header) < 32:
				break
			else:
				headers.append(process_header(header))
				processed_packet = process_data(body)
				x_pol.append(processed_packet[0])
				y_pol.append(processed_packet[1])
	
	f.close()
	print(len(headers))
	print('done!')