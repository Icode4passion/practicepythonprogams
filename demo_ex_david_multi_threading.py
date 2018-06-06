import logging
from threading import Thread
from time import sleep
from timeit import timeit
from random import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(threadName)-11s %(message)s')
log = logging.getLogger(__name__)
NUM_COUNTERS = 3
COUNT_TO = 5


def count_and_sleep():
    for n in range(COUNT_TO):
        seconds = random() / 2
        log.info('%2d. Waiting %.2f seconds.' % (n + 1, seconds))
        sleep(seconds)


def use_the_main_thread():
    for n in range(NUM_COUNTERS):
        count_and_sleep()


def use_multiple_threads():
    threads = [Thread(target=count_and_sleep) for n in range(NUM_COUNTERS)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


log.info('All in the main thread')
seconds = timeit(use_the_main_thread, number=1)
log.info('Completed in %.2f seconds' % seconds)

log.info('')
log.info('With multiple threads')
seconds = timeit(use_multiple_threads, number=1)
log.info('Completed in %.2f seconds' % seconds)



class Paddle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 80

    def draw(self):
        print('Drawing at %d, %d' % (self.x, self.y))

    def move(self, amount):
        self.y += amount

left_paddle  = Paddle(10, 10)
left_paddle.draw()
right_paddle = Paddle(400, 10)
right_paddle.draw()

left_paddle.move(1)
left_paddle.draw()