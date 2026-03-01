def polite_decorator(func):
    
    # Теперь обертка готова принять что угодно!
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
    return a + b


print(add(5, 7))