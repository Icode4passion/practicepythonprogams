def fizzbuzz(num):
	for i in range(num):
		

		if i %3 == 0 and i % 5 == 0 :
			print('fizzbuzz'+ str(i))

		elif i%3 == 0:
			print('fizz')

		elif i%5 == 0:
			print('Buzz')

		else :
			print(str(i))

		 


f = (fizzbuzz(50))
print (f)