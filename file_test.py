# # # 

# # # import pathlib
# # # path = pathlib.Path('C:User/usunkesu/Desktop/desktop/pypro/add.txt')
# # # if path.is_file():
# # # 	print("exists")
# # # else:
# # # 	print("not")


# # def square():
# # 	i = 1
# # 	while True:
# # 		yield i*i
# # 		i +=1

# # for n in square():
# # 	if n >20:
# # 		break
# # 	print(n)

# # def num():
# # 	ls = [x for x in range(1,100)]
# # 	yield ls
# # gen = num()

# gen = (x for x in range(1,100))
# print(gen)
# print(next(gen,None))

# dic = {x:x**2 for x in range(1,5)}
# print(dic)



num_list = [500, 600, 700]
alpha_list = ['x', 'y', 'z']


def nested_loop():
    for number in num_list:
        print(number)
        for letter in alpha_list:
            print(letter)

if __name__ == '__main__':
    nested_loop()