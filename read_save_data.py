import read_data as RD

#Create 7 files for 7 tiles
fh1 = open('/home/dl/Projects/SWAN/Programs/SWAN-git/tile_data/VELA01', 'w')
fh2 = open('/home/dl/Projects/SWAN/Programs/SWAN-git/tile_data/VELA02', 'w')
fh3 = open('/home/dl/Projects/SWAN/Programs/SWAN-git/tile_data/VELA03', 'w')
fh4 = open('/home/dl/Projects/SWAN/Programs/SWAN-git/tile_data/VELA04', 'w')
fh5 = open('/home/dl/Projects/SWAN/Programs/SWAN-git/tile_data/VELA05', 'w')
fh6 = open('/home/dl/Projects/SWAN/Programs/SWAN-git/tile_data/VELA06', 'w')
fh7 = open('/home/dl/Projects/SWAN/Programs/SWAN-git/tile_data/VELA07', 'w')

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
			tile = RD.process_header(header)[0][6:]
			processed_packet = RD.process_data(body)
			if tile == '01':
				for x, y in zip(processed_packet[0], processed_packet[1]) :
					fh1.write(str(x) + ' ' + str(y) + '\n')
			if tile == '02':
				for x, y in zip(processed_packet[0], processed_packet[1]) :
					fh2.write(str(x) + ' ' + str(y) + '\n')
			if tile == '03':
				for x, y in zip(processed_packet[0], processed_packet[1]) :
					fh3.write(str(x) + ' ' + str(y) + '\n')
			if tile == '04':
				for x, y in zip(processed_packet[0], processed_packet[1]) :
					fh4.write(str(x) + ' ' + str(y) + '\n')
			if tile == '05':
				for x, y in zip(processed_packet[0], processed_packet[1]) :
					fh5.write(str(x) + ' ' + str(y) + '\n')
			if tile == '06':
				for x, y in zip(processed_packet[0], processed_packet[1]) :
					fh6.write(str(x) + ' ' + str(y) + '\n')
			if tile == '07':
				for x, y in zip(processed_packet[0], processed_packet[1]) :
					fh7.write(str(x) + ' ' + str(y) + '\n')
		if i%50000 == 0: print("On packet number", i)
			
f.close()
fh1.close()
fh2.close()
fh3.close()
fh4.close()
fh5.close()
fh6.close()
fh7.close()

print('done!')