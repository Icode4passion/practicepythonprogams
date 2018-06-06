def afun(insideFunc):
        def awrapper(*args):
                print("Doing some stupid stuff")
                print("Calling inside function")
                insideFunc(*args)
        return awrapper

@afun
def valfunc(n,m,x):
        print("I live in hell")
        print(n*m+x)

valfunc(2,11,9)
