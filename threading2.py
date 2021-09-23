from time import sleep, time
from threading import Thread
from multiprocessing import Process
import sys

c = sys.argv[1]

concurrent = Thread if c == 'thread' else Process
print(concurrent)
start = time()

def foo():
    sleep(5)

p1 = concurrent(target=foo)
p1.start()
p1.join()
