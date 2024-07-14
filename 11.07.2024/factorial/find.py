import threading
import time
import random
import math

numbers_file_path = 'numbers.txt'
prime_numbers_file_path = "prime_numbers.txt"
factorials_file_path = "factorials.txt"

num_count = 1000
max_num = 20  # Ограничиваем значение для факториалов

file_ready_event = threading.Event()


def generate_random_numbers():
    with open(numbers_file_path, 'w') as f:
        for _ in range(num_count):
            f.write(f"{random.randint(1, max_num)}\n")
    print("Файл заполнен случайными числами.")
    file_ready_event.set()  # Сигнализируем, что файл готов


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def find_prime_numbers():
    file_ready_event.wait()  # Ждем сигнала, что файл готов
    primes = []
    with open(numbers_file_path, 'r') as f:
        for line in f:
            num = int(line.strip())
            if is_prime(num):
                primes.append(num)
    with open(prime_numbers_file_path, 'w') as f:
        for prime in primes:
            f.write(f"{prime}\n")
    print(f"Найдено {len(primes)} простых чисел.")


def calculate_factorials():
    file_ready_event.wait()  # Ждем сигнала, что файл готов
    factorials = []
    with open(numbers_file_path, 'r') as f:
        for line in f:
            num = int(line.strip())
            factorial_result = None
            try:
                factorial_result = math.factorial(num)
                factorials.append((num, factorial_result))
            except Exception as e:
                print(f"Ошибка при вычислении факториала для {num}: {e}")

    with open(factorials_file_path, 'w') as f:
        for num, factorial in factorials:
            f.write(f"{num}! = {factorial}\n")
    print(f"Вычислено {len(factorials)} факториалов.")


thread1 = threading.Thread(target=generate_random_numbers, name="Generator")
thread2 = threading.Thread(target=find_prime_numbers, name="PrimeFinder")
thread3 = threading.Thread(target=calculate_factorials, name="FactorialCalculator")


start = time.time()

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

finish = time.time()

# Статистика
res = finish - start
res_msec = res * 1000

print('Все потоки завершены')
print(f'Время работы в миллисекундах: {res_msec}')
print(f'Результаты простых чисел сохранены в файле: {prime_numbers_file_path}')
print(f'Результаты факториалов сохранены в файле: {factorials_file_path}')
