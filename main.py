import threading
import time


class Treading(threading.Thread):
    pass


def get_data(data):
    while True:
        print(f"<<< {threading.current_thread().name}: {data} >>>")
        time.sleep(1)


thr = threading.Thread(target=get_data, args=(str(time.time()),), name="Thread_1")
thr.start()

for i in range(100):
    print(f'Number in range: {i}')
    time.sleep(1)