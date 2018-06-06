##class address(object):
##    def __init__(self,fname,lname):
##        self.fname = fname
##        self.lname = lname
##    @property
##    def fullname(self):
##        return self.fname + self.lname
##
##ad = address('rad','sya')
##print(ad.fullname)



def func(f):
    def func2():
        print("Doing something in func2 for func")
        f()
    return func2

@func
def f1():
    print("Adding")
f1()
    
        

        
        

