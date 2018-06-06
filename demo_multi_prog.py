import threading
import os

def task1():
	print("Task 1 has the thread with name {}".format(threading.current_thread().name))
	print("Id of Process running task1 : {}".format(os.getpid()))

def task2():
	print("Task 2 has the thread with name {}".format(threading.current_thread().name))
	print("Id of Process running task2 : {}".format(os.getpid()))


if __name__ == '__main__':
	
	print("Main thread with name {}".format(threading.main_thread().name))
	print("Id of Process running main thread {}".format(os.getpid()))


	t1 = threading.Thread(target = task1 , name = "task 1")
	t2 = threading.Thread(target = task2 , name = 'task 2')

	t1.start()
	t2.start()

	t1.join()
	t2.join()

print(threading.active_count())
print(threading.enumerate())