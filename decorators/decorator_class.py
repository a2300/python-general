import functools

class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0 # Здесь мы храним состояние (счетчик)
        
        # Аналог @wraps для классов, чтобы не потерять имя и докстринг
        functools.update_wrapper(self, func) 

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Функция {self.func.__name__} была вызвана {self.count} раз(а)")
        
        # Вызываем оригинальную функцию и возвращаем результат
        return self.func(*args, **kwargs)

@CallCounter
def say_hi(name):
    print(f"Привет, {name}!")

say_hi("Алексей")
say_hi("Анна")
say_hi("Иван")