##n = int(input("Enter the N digit"))
##
##ns = str(n)
##
##t1 = ns + ns
##
##t2 = ns + ns + ns
##
##add = int(ns) + int(t1) + int(t2)
##
##print("Sum =" ,add)
##
##
##############***************


##n = int(input("Enter a NUmber"))
##rev = 0
##while(n>0):        
##	dig = n%10
##	rev = rev*10+dig
##	n= n//10
##print("Reversr number ",rev)


def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)
