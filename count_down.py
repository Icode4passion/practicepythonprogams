import time
def countdown(n):
    while n:
        mins,sec = divmod(n,60)
        timeformat = "{:02d} min:{:02d} sec".format(mins,sec)
        print 'timeformat \r'
        time.sleep(1)
        n -=1
    print "GoodBye"

countdown(20)
