def my_dec_function(pass_func):
	def inside_function():
		num = 10
		if num == 10:
			print "True"
		else :
			print "False"
		pass_func()
	return inside_function

def out_side_func():
	print "I am outside function"


out_side_func =my_dec_function(out_side_func)

out_side_func()

print "#" * 30

@my_dec_function
def dec_function():
	print "My name is Decorator @"

dec_function()
