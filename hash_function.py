# def hash(astring , tablesize):
# 	sum = 0
# 	for pos in range(len(astring)):
# 		print pos
# 		sum = sum + (ord(astring[pos]))
# 		print sum 
	
# 	return sum%tablesize

# hash_func = hash("54",11)

# print hash_func


lst = [113,117,97,100,114,108,116,105,99]

def result(ls):
	temp = []
	for i in ls:
		return i % 11
	#return temp

print  result(lst)
#print list (res)
