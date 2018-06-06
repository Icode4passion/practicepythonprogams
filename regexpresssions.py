import re

result = re.match(r'Am','Am I Am a BAm in the Am')
print(result)


res = re.search(r'Am' , 'Am I Am a BAm in the Am')
print(res)


r = re.findall(r'Am' , 'Am I Am a BAm in the Am')
print(r)

# pre = re.findall(r'\d+', 'apple2 is a good3 company43 who pays 34doller to Wip40')
# #print(pre)

# email = re.findall(r'\w+@','yogeerama@gmail.com   g@c.co g11_2@pt.org')
# print(email)



resp = re.findall(r'\d{2}-\d{2}-(\d{4})', "I was born in 12-12-0011 which is just befor e JC 12-34-2001 233-33-2345 number")
print(resp)



stink = 'blue ali-khan@gmail.com monkey donkey'
respr = re.search(r'[\w.-]+@[\w.]+',stink)
print(respr.group(2))