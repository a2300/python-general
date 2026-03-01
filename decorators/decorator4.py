def polite_decorator(func):
    def wrapper():
        print("Hi, start working")
        func()
        print("End working")
    
    return wrapper

def work():
    print("Fixing bugs")


work = polite_decorator(work)
work()
