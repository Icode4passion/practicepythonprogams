# import re

# reg = "abcxyz"
# if  re.search('\d+',reg):
# 	print "Match found"
# else :
# 	print "Match not found"


# regex = r"[a-zA-Z]+ \d+"
# rex = re.findall(regex, "June 24 , Aug 30, December 12")
# for r in rex:
# 	print "Full match : %s"%(r)
import re

regex = re.compile(r'(\w+) World')
result = regex.search('Hello World is the first Prog')
if result :
	print "Match found"
else :
	print "Match not found"

for result in regex.findall("Hello World , Hi World , Welcome World"):
	print result
