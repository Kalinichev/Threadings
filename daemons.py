import time
import threading


def get_data(data):
    while True:
        print(f'<<< [{threading.current_thread().name}] -- {data} >>>')
        time.sleep(1)


thr = threading.Thread(target=get_data, args=(str(time.time()),), name=f'Thread', daemon=True)

thr.start()
time.sleep(2)
print('finish')
