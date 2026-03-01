def make_multipler(n):
    # Создаем внутреннюю функцию
    def multiplier(x):
        return x * n
    
    # Возвращаем саму функцию, а не результат ее работы! (без скобок)
    return multiplier

three_times = make_multipler(3)
print(three_times(10))  # Выведет 30
print(three_times(5))  # Выведет 15