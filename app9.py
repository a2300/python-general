# https://habr.com/ru/articles/982534/

def increment(count=0):
    count += 1  # Создается НОВОЕ число, локальная переменная count теперь ссылается на него
    return count

def add_item_wrong(item, storage=[]):
    storage.append(item)
    return storage

def add_item_correct(item, storage=None):
    if storage is None:
        storage = []
    storage.append(item)
    return storage

print("Incrementing. Immutable objects")
print(increment()) # 1
print(increment()) # 1 (в __defaults__ по-прежнему лежит старый 0)

print("Incrementing. Mutable objects (list). Incorrect")
print(add_item_wrong("яблоко"))  # Вывод: ['яблоко']
print(add_item_wrong("банан"))   # Вывод: ['яблоко', 'банан']
print(add_item_wrong("груша"))   # Вывод: ['яблоко', 'банан', 'груша']

print("Incrementing. Mutable objects (list). Correct")
print(add_item_correct("яблоко"))  # Вывод: ['яблоко']
print(add_item_correct("банан"))   # Вывод: ['банан']
print(add_item_correct("груша"))   # Вывод: ['груша']