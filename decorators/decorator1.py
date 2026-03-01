def greering():
    print("Hello, World!")

# Присваиваем функцию переменной. 
# ВАЖНО: мы пишем имя без скобок! Мы не вызываем функцию, мы ее передаем.
say_hello = greering

# Теперь say_hello делает то же самое, что и greet
say_hello()
# Output:
# Hello, World!