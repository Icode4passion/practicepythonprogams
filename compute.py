#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

inp = int(raw_input('Enter the numer desired :'))

def sum(num):
	nnn =  num + (num *10) + (num * 100)
	nn = num + (num * 10)
	n = num

	return nnn + nn + n


print sum(inp)

