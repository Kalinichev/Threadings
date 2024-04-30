import time
import threading

value = 0

locker = threading.Lock()


# locker = threading.RLock() то же, но locker.release() может выполянить только тот, кто делал locker.acquire()


def inc_value():
    global value
    while True:
        locker.acquire()
        value += 1
        time.sleep(0.1)
        print(value)
        locker.release()


for i in range(5):
    threading.Thread(target=inc_value).start()
