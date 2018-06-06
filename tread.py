import threading 
import os

def foo():
	print ("thread 1"+" "+threading.current_thread().name)
	#print(t1.is_alive())



def bar():
	print('thread 2')


if __name__ == '__main__':
	print("In Main Thread"+" "+threading.main_thread().name)
	t1 = threading.Thread(target = foo , name = "foo")
	t2 = threading.Thread(target = bar , name = bar)


	t1.start()
	t2.start()
	