#https://github.com/ONETAPL3G3ND
import time
from functools import lru_cache

def fibonacci_no_cache(n):
    if n < 2:
        return n
    return fibonacci_no_cache(n-1) + fibonacci_no_cache(n-2)

@lru_cache(maxsize=None)
def fibonacci_with_cache(n):
    if n < 2:
        return n
    return fibonacci_with_cache(n-1) + fibonacci_with_cache(n-2)

def measure_time(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return result, end_time - start_time

if __name__ == "__main__":
    n = 35

    result_no_cache, time_no_cache = measure_time(fibonacci_no_cache, n)
    print(f"Без кэширования: Число Фибоначчи {n} = {result_no_cache}, время = {time_no_cache:.4f} секунд")

    result_with_cache, time_with_cache = measure_time(fibonacci_with_cache, n)
    print(f"С кэшированием: Число Фибоначчи {n} = {result_with_cache}, время = {time_with_cache:.4f} секунд")

    if time_with_cache > 0:
        speedup = time_no_cache / time_with_cache
        print(f"Ускорение за счет кэширования: {speedup:.2f} раз")
    else:
        print("Время выполнения с кэшированием слишком мало для измерения.")
