def polite_decorator(func):
    def wrapper():
        print("Hi, start working")
        func()
        print("End working")
    
    return wrapper

@polite_decorator
def work():
    print("Fixing bugs")


work()