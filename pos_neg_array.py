def bubbleSort(alist):
	for passnum in range(len(alist)-1,0,-1):
		for i in range(passnum):
			if alist[i] > alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp

alist = [52,23,93,17,31,44,55,20,34,67,89,05,23,14,67,89,45,100]

bubbleSort(alist)
print alist[-2:]