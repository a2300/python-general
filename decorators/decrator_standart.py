from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # ... что-то делаем ДО ...
        result = func(*args, **kwargs)
        # ... что-то делаем ПОСЛЕ ...
        return result
    return wrapper