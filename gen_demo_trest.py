class Item(object):
	def __init__(self,name,value):
		self.name = name 
		self.value = value

	def __str__(self):
		return "{} is the item with Value {} ".format(self.name ,self.value)

	@property
	def display(self):
		return self.name #+ " " + self.value

	@display.setter
	def display(self,value):
		self.name = value


it1 = Item("Soap",10)
print(it1)
print(it1.name)
print(it1.value)
print(it1.display)