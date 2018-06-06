def power(num,rad):
	if rad == 0:
		return 1
	if num == 0:
		return 0
	else :
		return num * power(num,rad-1)


p =power(num = 0,rad = 10)
print (p)