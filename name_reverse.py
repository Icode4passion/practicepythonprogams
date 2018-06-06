# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

f_name = raw_input("Enter Your First Name : ")
l_name = raw_input("Enter Your Last Name : ")

def fullname(fname,lname):
	full_name = fname +" " + lname
	return "My Full name is :" +  full_name

def reverse_name(fname,lname):
	name = fname +" " + lname
	r_name = name[::-1] 
	return "My reverse name :" + r_name

print fullname(f_name,l_name)

print reverse_name(f_name,l_name)