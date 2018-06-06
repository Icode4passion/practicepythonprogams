def fact_numb(x) :
	print "The factoria of number {} are".format(x)
	for i in range(1,x+1):
		if x % i == 0:
			print i

num = 20
fact_numb(num)

import pdb; pdb.set_trace()
fact_numb(num)
