num = 181
flag =0

for i in range(1,num+1):
	if (i*(i+1)==num):
		flag = 1
		break
if flag == 1 :
	print "Number is Pronic"
else  :	
	print "number is not pronic" 