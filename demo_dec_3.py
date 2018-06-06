def first_name(func):
	def fwrapper(name):
		return "<i> {0} </i>".format(func(name))
	return fwrapper

def last_name(func):
	def lwrapper(name):
		return "<b> {0} </b>".format(func(name))
	return lwrapper

def dec_name(func):
	def awrapper(name):
		return "@ {0} @".format(func(name))
	return awrapper

@dec_name
@first_name
@last_name
def test(name):
	return name


print (test("John"))
