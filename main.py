import threading
import time


class Treading(threading.Thread):
    pass


def get_data(data):
    print(f"<<< {threading.current_thread().name}: {data} >>>")
    time.sleep(5)


thr = threading.Thread(target=get_data, args=(str(time.time()),), name="Thread_1")
thr.start()
