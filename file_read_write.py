with open("openfile.txt",'w+') as fp:
	for i in range(0,10):
		fp.write("This is the Line {} \n".format(i+1))

