# import time

# time_lst = (time.localtime())

# utime = str(input("Enter the time in 24 hours format"))

# if utime != str(time_lst[3]):
# 	print("Wake up")
# else :
# 	print(utime)
# 	print(time_lst[3])
# 	print("Sleep")

 


# from datetime import datetime
# now = datetime.now()
# print(type(now.hour))
# cutime = input("Enter the time you want")
# print(type(cutime))
# if now.hour == int (cutime):
# 	print("wake up")
# else :
# 	print("Sleep")




ss = """You could """ # create a dictionary with characters as keys and counters as the corresponding values. The first time you see a character, you would add an item to the dictionary. After that you would increment the value of an existing item."""

data = dict()
#words = ss.split()
#print (len(words))
for word in ss:
	if word not in data:
		data[word] = 1
	else :
		data[word] = data[word] + 1

print (data)