lst = [1,2,[3,4,5],6,[7,8,9,[11,12,['a','b'],],0],['q','w','e']]

def mulList(ls):
	for l in ls:
		if type(l) == 'list':
			print (l)
			break
		print (l)
mulList(lst)