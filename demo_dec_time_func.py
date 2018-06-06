import time

def timing_function(some_function):
	def wrapper_time():
		t1 = time.time()
		some_function()
		t2 = time.time()
		return "Time taken {}".format(str(t2-t1))
	return wrapper_time

@timing_function
def calFunc():
	num = []
	for n in range(0,1000):
		num.append(n)
	print("sum of number are :{}".format(str(sum(num))))

print(calFunc())
