def some_function(passing_function):
	def wrapper_function():
		print("Inside Wrapper")
		passing_function()
	return wrapper_function

@some_function
def passing_function():
	print("I am a passing function")

passing_function()