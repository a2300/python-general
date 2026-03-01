from functools import wraps

def polite_decorator(func):
    
    # Теперь обертка готова принять что угодно!
    @wraps(func) # <--- Указываем, чьи метаданные нужно скопировать
    def wrapper(*args, **kwargs):
        print("Hi, start working")
        
        # Передаем все собранные аргументы в оригинальную функцию
        # Ловим результат работы оригинальной функции
        result = func(*args, **kwargs)
        print("End working")
        
        # Честно отдаем его наружу
        return result
    
    return wrapper

@polite_decorator
def add(a, b):
    """Складывает два числа и возвращает результат."""
    return a + b


print(add(5, 7))
print(add.__name__)
print(add.__doc__)