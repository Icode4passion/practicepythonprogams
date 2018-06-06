from library import Base

assert hasattr(Base,"foo") , "your code is broken"

class Derived(Base):
	def bar(self):
		return self.foo()

d = Derived()
print (d)