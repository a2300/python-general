class PositiveNumber:
    """Дескриптор для проверки положительных чисел"""
    
    def __set_name__(self, owner, name):
        # Автоматически сохраняем имя атрибута (например, _price)
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"Значение не может быть отрицательным!")
        setattr(instance, self.private_name, value)

class Product:
    # Применяем дескриптор ко всем нужным полям на уровне класса
    price = PositiveNumber()
    weight = PositiveNumber()
    discount = PositiveNumber()

    def __init__(self, price: float, weight: float):
        self.price = price
        self.weight = weight

item = Product(100, 2.5)
item.price = -10  # ValueError: Значение не может быть отрицательным!