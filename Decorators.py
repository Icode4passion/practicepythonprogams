def repeater(old_function):
    def new_function(*args, **kwargs):
        old_function(*args,**kwargs)
        #old_function(*args,**kwargs)
    return new_function

@repeater
def Multiply(num1,num2):
    print (num1*num2)

Multiply(3,4)


# tuple = (1,2,3,4,{'one':'a','two':'b'},'abbe',[1,2,3,4])
# # print tuple[4]['a']='ee'
# # print tuple[5]="tre"
# print tuple[6][0] = 7
# dict = {'one':"a",'two':"b"}
# print dict['one']














##t = (1,1.0,'True',True,[1,2,3,4],{0,9,8},{'a':1,'b':4})
##print t
##
##
##t[4][3] = 'q' 
##
##print t
##
##l = [1,2,3,(6,7),"true"]
##l[4]  = "ram"
##print l
##
##
##
##
##
