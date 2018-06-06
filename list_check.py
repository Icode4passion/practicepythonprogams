#def list_check(lst):
#	if lst == []:
#		return #True

#li = []
#ls = [1,2]

#print (list_check(li))
#list_check(ls)



def list_check(lst):
	for l in lst:
		if type(l) == dict and len(l) == 0:
			print ("List has Dict and it is empty")
		elif type(l) == dict and len(l) !=0:
			print ("List has Dict and it is not empty")

lsy = [{1:2,"a":2},{1:1},{0:'l'},{}]

#list_check(lsy)


def list_list(lst):
	for l in lst:
		if type(l) == list:
			#s = []
			#s= sum(l)
			#print (l)
			for s in l:
				print(s)
			
		
		else:
			print (l)
		
			
	
ls = [[1,2,3],[6,1,2],[43,2,1],[1,1,1,[1,2]]]
list_list(ls)

		
	

			