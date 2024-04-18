import threading
import time


class Treading(threading.Thread):
    pass


def get_data(data):
    while True:
        print(f"<<< {threading.current_thread().name}: {data} >>>\n")
        time.sleep(1)


thr = threading.Thread(target=get_data, args=(str(time.time()),), name="Thread_1")
thr.start()


print('old_name:', threading.main_thread().name)
threading.main_thread().name = 'result'
print('new_name:', threading.main_thread().name)

for i in range(100):
    print(f'Number in range: {i}')
    time.sleep(1)

    if i % 10 == 0:
        print('active threads', threading.active_count())
        print('enumerate:', threading.enumerate())
        print('Thread_1 is alive:', thr.is_alive())
