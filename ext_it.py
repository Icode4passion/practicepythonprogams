# # import init_et

# # sree = init_et.Student(12,"Sree","X")
# # sree.disp()

# # file_name = "./new_txt.txt"

# # with open(file_name,'wt') as fp:
# # 	print("My Name __", file = fp)

# file_name = "new.bin"

# with open(file_name , 'wb') as fp:
# 	text = "Hello World"
# 	fp.write(text.encode('utf-8'))


# import array
# a = array.array()
 
class Pair(object):
 	def __init__(self,x,y):
 		self.x =x
 		self.y = y

 	def __repr__(self):
 		return "Pair({0.x!r},{0.y!r})".format(self)

 	def __str__(self):
 		return  '({0.x!s},{0.y!s})'.format(self)

p = Pair(2,3)

print(p)