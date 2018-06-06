from time import sleep

def sleep_decorator(function):
	def wrapper(*args,**kwargs):
		sleep(2)
		return function(*args,**kwargs)
	return wrapper


@sleep_decorator
def print_num(num):
	return num

print print_num(45)

for num in range(6):
	print print_num(num)