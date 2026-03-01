import time
from functools import wraps

def benchmark(func):
    """Декоратор для замера времени выполнения функции."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        
        run_time = end_time - start_time
        print(f"[Timer] Функция {func.__name__} отработала за {run_time:.4f} сек.")
        return result
    return wrapper

@benchmark
def process_large_data():
    time.sleep(1.2) # Эмулируем тяжелую работу
    return "Готово"

process_large_data()
# Вывод: [Timer] Функция process_large_data отработала за 1.2014 сек.