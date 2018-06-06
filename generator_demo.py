def func(num):
	for i in num:
		print i * i

lst = [1,2,3,4,5]

print func(lst)


lam = lambda x : "True" if x >3 else "False" 
print lam(10)