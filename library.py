import pdb

num = [1,2,3,4]
alpha = ['a','e','i','o','u']

def num_alpha():
	for n in num:
		print (n)

		#pdb.set_trace()

		for alp in alpha:
			print(alp)

if __name__ == '__main__':
	num_alpha()
