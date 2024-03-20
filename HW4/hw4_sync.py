
from random import randint
import time


ARRAY_LEN = 2000000  # размер списка
MAX_RANDOM = 100 + 1  # максимальное значение случайного числа

test_array = [randint(1, MAX_RANDOM) for _ in range(ARRAY_LEN)]


def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        print(f'Время выполнения {execution_time:.2f} ')
        return result

    return wrapper


@calculate_time
def summ_sync(user_array):
    summ = 0
    for num in user_array:
        summ += num
    return summ




if __name__ == '__main__':
    print(f'Sync: {summ_sync(test_array)}')




