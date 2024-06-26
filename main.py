import threading
import time


def get_data(data, value):
    for _ in range(value):
        print(f"<<< {threading.current_thread().name}: {data} >>>")
        time.sleep(1)


thr_list = []

for i in range(4):
    thr = threading.Thread(target=get_data, args=(str(time.time()), i,), name=f'Thread_{i}')
    thr_list.append(thr)
    thr.start()

for i in thr_list:
    i.join()

print(thr_list)
print('Finish')
#
# print('old_name:', threading.main_thread().name)
# threading.main_thread().name = 'result'
# print('new_name:', threading.main_thread().name)
#
# for i in range(100):
#     print(f'Number in range: {i}')
#     time.sleep(1)
#
#     if i % 10 == 0:
#         print('active threads', threading.active_count())
#         print('enumerate:', threading.enumerate())
#         print('Thread_1 is alive:', thr.is_alive())
