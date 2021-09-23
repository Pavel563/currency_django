import threading
from time import sleep, time
# from threading import Thread

# def foo(sleep_time, ):
#     sleep(sleep_time)
#     print(f'Thread Ended: {threading.current_thread()}')

# from concurrent.futures import ThreadPoolExecutor
#
# wiki_page_urls = [
#     "https://en.wikipedia.org/wiki/Ocean",
#     "https://en.wikipedia.org/wiki/Island",
#     "https://en.wikipedia.org/wiki/this_page_does_not_exist",
#     "https://en.wikipedia.org/wiki/Shark",
# ] * 30
#
# import requests
# start = time()

# for url in wiki_page_urls:
    # requests.get(url)

# futures = []
# with ThreadPoolExecutor(max_workers=6) as executor:
#     for url in wiki_page_urls:
#         futures.append(executor.submit(requests.get, url))
#
# for future_ in futures:
#     future_.result()
#
# print(f'End. {time() - start}')

# print('Start')
# start = time()
#
# threads = []
#
# for sleep_time in range(1, 10_000):
#     # thr = Thread(target=foo, args=[sleep_time])  # foo(sleep_time)
#     thr = Thread(target=foo, kwargs={'sleep_time': 5})  # foo(sleep_time=sleep_time)
#     # Thread(target=bar, args=[1, 2, 3], kwargs={"a": "b", "c": "d"})  # bar(1, 2, 3, a="b", c="d")
#     threads.append(thr)
#     thr.start()
#
# for thread in threads:
#     thread.join()
#
# print(threading.current_thread())
# print(f'End. {time() - start}')

# print('Start')
# start = time()
# foo()
# foo()
# print(f'End. {time() - start}')

from threading import Thread
from multiprocessing import Process

start = time()
NUM = 1_000_00000
# while NUM:
#     NUM -= 1
def foo(counter):
    while counter:
        counter -= 1

# foo(NUM)
p1 = Process(target=foo, args=[int(NUM / 2)])
p2 = Process(target=foo, args=[int(NUM / 2)])
p3 = Process(target=foo, args=[int(NUM / 2)])
p4 = Process(target=foo, args=[int(NUM / 2)])
p1.start()
p2.start()
p3.start()
p4.start()
p1.join()
p2.join()
p3.join()
p4.join()
print(f'End. {time() - start}')
