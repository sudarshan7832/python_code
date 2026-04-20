def change_behavior(func):
    def wrapper(a, b):
        c = 1
        return a - b + c
    return wrapper

@change_behavior
def add(a, b):
    return a + b

print(add(10, 2))