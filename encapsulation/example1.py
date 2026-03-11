class Order:
    def __init__(self, amount: float):
        self.amount = amount
        # Внутреннее состояние, которое не должно меняться снаружи напрямую
        self._discount = 0.0  

    def apply_promocode(self, code: str):
        """Публичный метод для работы со скидкой"""
        if code == "HABR":
            self._discount = self.amount * 0.2
        # здесь могла бы быть сложная логика походов в БД или проверок

    def get_final_price(self) -> float:
        return self.amount - self._discount

order = Order(1000)
print(order.get_final_price())

order2 = Order(1000)
# Питон не выдаст никаких ошибок
order2._discount = 9999.0  
print(order2.get_final_price())  # Выведет: -8999.0. Бизнес в убытках.