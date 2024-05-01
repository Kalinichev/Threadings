import threading
import time
import random
from threading import current_thread

bar = threading.Barrier(5)


def test(barrier):
    slp = random.randint(3, 8)
    time.sleep(slp)
    print(f'Поток {current_thread().name} запущен в {time.ctime()}')
    barrier.wait()
    print(f'Поток {current_thread().name} преодолел барьер в {time.ctime()}')


for i in range(5):
    threading.Thread(target=test, name=f'Thread - {i}', args=(bar,)).start()
