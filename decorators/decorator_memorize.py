from functools import wraps

def memoize(func):
    """Кэширует результаты выполнения функции."""
    cache = {} # Здесь будем хранить уже вычисленные результаты
    
    @wraps(func)
    def wrapper(*args):
        # В качестве ключа используем переданные аргументы
        if args in cache:
            print(f"[Cache] Беру результат для {args} из памяти")
            return cache[args]
            
        print(f"[Compute] Вычисляю результат для {args}...")
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10)) 
# Вывод: покажет цепочку "Вычисляю...", а затем множество "Беру результат из памяти"