# class A(object):
# 	def f(self):	
# 		return self.g()
# 	def g(self):
# 		return "A"

# class B(A):
# 	def g(self):
# 		return "B"

# a = A()
# b = B()

# print a.f(),a.g()
# print b.f(),b.g()


def powerOf2(k):
	if k == 0:
		return 1
	else :
		return 2**powerOf2(k-1)

print powerOf2(3)
