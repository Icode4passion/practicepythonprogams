datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for data in datalist:
	print type(data)


for num in range(0,6):
	if num == 3:
		continue

	elif num == 26:
		break
	print num


print "@@" *6

for i in range(1,50):
	if i%3 ==0 and i%5 ==0:
		print 'Fizzbuzz'
		continue

	elif i%3 ==0 :
		print "Fizz"
		continue

	elif i % 5 ==0 :
		print "Buzz"
		continue

	print i