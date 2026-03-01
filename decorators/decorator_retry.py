import time
from functools import wraps

def retry(times=3, delay=1, exceptions=(Exception,)):
    """
    Повторяет выполнение функции при возникновении определенных исключений.
    :param times: количество попыток
    :param delay: пауза между попытками (в секундах)
    :param exceptions: кортеж с исключениями, которые нужно перехватывать
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"[{func.__name__}] Ошибка {type(e).__name__}: {e}.")
                    if attempt == times:
                        print("Все попытки исчерпаны. Падаем.")
                        raise
                    print(f"Ждем {delay} сек. и пробуем снова (Попытка {attempt + 1}/{times})...")
                    time.sleep(delay)
        return wrapper
    return decorator

# Перехватываем только ошибки соединения
@retry(times=3, delay=2, exceptions=(ConnectionError, TimeoutError))
def fetch_api_data():
    # ... тут логика похода в сеть ...
    raise ConnectionError("Сервер разорвал соединение")
