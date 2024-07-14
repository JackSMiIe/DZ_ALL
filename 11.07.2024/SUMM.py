import threading
import time
from random import randint as r

sum_result = None
average = None
arr = None
arr_ready = threading.Event()


def arr_1():
    global arr
    arr = [r(99, 10_000) for i in range(500_000)]
    print('One')
    arr_ready.set()  # массив готов


def summ_result():
    global average
    arr_ready.wait()  # Ждем что массив готов
    average = sum(arr)
    print('Two')


thread1 = threading.Thread(target=arr_1, name="Массив")
thread2 = threading.Thread(target=summ_result, name="Сумма")

start = time.time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

finish = time.time()

print('Все потоки завершены')
print('Список:', arr[:10])
print('Сумма:', average)

res = finish - start
res_msec = res * 1000
print('Время работы в миллисекундах: ', res_msec)
