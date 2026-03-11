class User:
    def __init__(self, login: str, password: str):
        self.login = login
        self.__password = password  # Якобы строгий private

user = User("habr_user", "super_secret")

print(user.login)       # Выведет: habr_user
# print(user.__password)  # Ошибка! ValueError Exception

print(user.__dict__)

# Получаем прямой доступ к "скрытому" атрибуту
print(user._User__password)  # Выведет: super_secret

# И даже можем его изменить
user._User__password = "new_password"