array = [13,6,2,17,73,45,6,90,4]

def linear_search(arr,ele):
	for i in range(len(arr)):
		if arr[i] == ele:
			print "Element found {} in at this index {}".format(ele,i)

linear_search(array,45)
