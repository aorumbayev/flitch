import os

def split_equal(filename:str, names:str, percentage:int):
	filename = "/Users/altynbekorumbayev/projects/flitch/flitch/test.txt"

	with open(filename, 'rb') as mfile:
		content = bytearray(os.path.getsize(filename))
		chunk_size = int(len(content) * percentage/100)
		mfile.readinto(content)

		for c, i in enumerate(range(0, len(content), chunk_size)):
			with open(filename + '_' + str(i), 'wb') as f:
				f.write(content[i: i + chunk_size])


split_equal('', '', 20)
