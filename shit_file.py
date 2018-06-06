filename = "shit.csv"

with open(filename, 'a+') as fp:
	fpr = fp.readlines()

for r in fpr :
	print (r)