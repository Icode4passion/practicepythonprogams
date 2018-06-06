#match()
# import re
# result = re.match(r'\d+',"AV Analytic Vidya AV")

# if result:
# 	print("Match found")
# else :
# 	print("Match not found")

#search
# import re
# result = re.search(r'AV','AV Analytics Vidya AV')

# if result:
# 	print("Search Found",result.group(0))
# else :
# 	print("Search Not Found")


#findall

# import re
# result = re.findall(r'AV', "Analytic Vidya AV and its AV with AV")
# print(result)


#split
# import re
# result = re.split(r'o',"India is One nation filled with fools",maxsplit= 1)
# print (result)


# #sub
# import re
# result = re.sub(r'One','one',"India is One nation filled with fools",flags=re.IGNORECASE)
# print(result)

#compile

import re
pattern = re.compile('\d+')
result = pattern.findall('Analytic vidhya is 1 of the 10 best machine learning sites in India fo ryear 2017')
print(result)