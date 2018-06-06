class MyClass(object):

    i = 123
    def __init__(self,x):
    	self.x = x

    def pint(self):
    	print(self.x)


     

# a = MyClass(21)
# a.pint()



class Student(object):

	def __init__(self,rln,name,std):
		self.name = name 
		self.rln = rln
		self.std = std

	def disp(self):
		print('{} {} {}'.format(self.rln,self.name,self.std))

	def modify(self,rln,std):
		self.rln = rln
		self.std = std



ram = Student(1,"Ram","I")
shilpa = Student(2,"Shilpa",'II')

ram.disp()
shilpa.disp()
shilpa.modify(3,"III")
shilpa.disp()


