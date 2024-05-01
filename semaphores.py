import time
import random
from threading import Thread, BoundedSemaphore, current_thread

max_threads = 5
pool = BoundedSemaphore(value=max_threads)


def test():
    with pool:
        slp = random.randint(1, 5)
        print(f'{current_thread().name} - sleeping {slp}')
        time.sleep(slp)


for i in range(10):
    Thread(target=test, name=f'thread-{i}',).start()
