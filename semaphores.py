import time
from threading import Thread, BoundedSemaphore, current_thread

max_threads = 5
pool = BoundedSemaphore(value=max_threads)


def test():
    with pool:
        print(current_thread().name)
        time.sleep(3)


for i in range(10):
    Thread(target=test, name=f'thread-{i}',).start()
