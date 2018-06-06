# def fact(n):
# 	if n == 0 :  # Breaking condition
# 		return 1
# 	else :
# 		return (n * fact(n-1))

# print(fact(5))


def sumofSquares(n):
	if n == 1 :
		return 1


	else :
		return n * n + sumofSquares(n - 1)

print (sumofSquares(5))