def shout():
    print("Ura!!!")

def whisper():
    print("Tsss")

def execute_twice(func):
    func()
    func()

execute_twice(shout)
print("\n")
execute_twice(whisper)