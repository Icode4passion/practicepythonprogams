from threading import Thread
import time
def work(num):
    print("Work {}".format(num))
    print(currentThread().getName())

def worker():
	print(currentThread().getName(),"Starting")
	time.sleep(2)
	print(currentThread().getName(),"Ending")

thread = []

for i in range(5):
    t = Thread(target = work , args=(i,))
    thread.append(t)
    w = Thread(target = worker , name = 'Worker')
    t.start()
    w.start()
    
# for th in thread:
# 	print(th)