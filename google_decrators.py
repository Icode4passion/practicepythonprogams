# def add(n1,n2):
# 	if validate_two_numbers(n1,n2):
# 		return n1+n2

# def multiply(n1,n2):
# 	if validate_two_numbers(n1,n2):
# 		return n1*n2

# def exponeential(n1,n2):
# 	if validate_two_numbers(n1,n2):
# 		import math
# 		return math.pow(n1,n2)


def is_num(n):
	try:
		float(n)
		return True
	except ValueError:
		return False


def validate_two_numbers(n1,n2):

	if not (is_num(n1) and is_num(n2)):
		return False
	return True


def validate_function(func):

	def wrapped_function(n1,n2):

		if not validate_two_numbers(n1,n2):
			raise Exception("Arguments must be numbers")

		return func(n1,n2)

	return wrapped_function


@validate_function
def add(n1,n2):
	return n1 + n2

try:
	add(1,'hi')
except Exception e:
	print ('Catc')

