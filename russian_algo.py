def russian(a,b):
    x,y = a,b
    z = 0
    while x > 0 :
    	if x % 2 == 1:z = z + y
    	y = y << 1
    	x = x >> 1
    return z

print (russian(2**10,2**5))