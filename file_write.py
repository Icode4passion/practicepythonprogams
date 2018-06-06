with open("openfile.txt",'w+') as fp:
	for i in range(0,20):
		fp.write("This is the Line {} \n".format(i+1))

with open('openfile.txt' , 'r+') as fp:
		contents = fp.readlines()
		for content in contents:
			print (content)

with open('openfile.txt' , 'a+') as fp:
	fp.write("\n This is an append operation \n")


with open("openfile.txt" ,'r+') as fp:
	file = fp.readlines()
	print("Total number of lines {}".format(len(file)))
	for f in file:
		#print(len(f))
		fsp = f.split()
		print (fsp)

#with open("open_file.txt", 'w+') as f:
