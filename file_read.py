def main(filename):

	with open(filename , 'r+') as fp:
		words = fp.read().split()
		# print(words)
		max_len = len(max(words,key=len))
		for word in words:
			if len(word) == max_len:
				print(word)
		

if __name__ == '__main__':
	main('openfile.txt')


with open('image.jpg' , 'rb+') as img:
	byte = img.read()
	while byte != "":
		byte = img.read(1)
	print (len(img.readlines()))