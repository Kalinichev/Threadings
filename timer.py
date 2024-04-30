import threading
import time


def somefunc():
    while True:
        print("Some_text")
        time.sleep(1)


thr = threading.Timer(5, somefunc)
thr.daemon = True
thr.start()

for _ in range(10):
    print('azazazazazazazazazazazazaz')
    time.sleep(1)

thr.cancel()

print('Finish')
