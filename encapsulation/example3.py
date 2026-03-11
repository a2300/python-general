class Account:
    def __init__(self, initial_balance: float):
        # Обратите внимание: мы используем сеттер прямо в __init__
        self.balance = initial_balance

    @property
    def balance(self) -> float:
        """Это геттер. Вызовется при чтении: print(acc.balance)"""
        return self._balance

    @balance.setter
    def balance(self, value: float):
        """Это сеттер. Вызовется при записи: acc.balance = 100"""
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным!")
        self._balance = value

acc = Account(100)

# Теперь мы работаем с balance как с обычным публичным атрибутом!
print(acc.balance)  # Выведет: 100
acc.balance += 50   # Выведет: 150
try:
    acc.balance = -10   # Выбросит ValueError: Баланс не может быть отрицательным!
except ValueError as e:
    print(f"Exception is caught {e}")

