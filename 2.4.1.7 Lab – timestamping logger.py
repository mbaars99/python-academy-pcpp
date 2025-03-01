from datetime import datetime

def print_timestamp(our_function):
    def wrapper(*args):
        timestamp = datetime.now()
        print(f"timestamp {our_function.__name__}(): {timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')}", end=" ")
        return our_function(*args)
    return wrapper

@print_timestamp
def add(a, b):
    return a + b

@print_timestamp
def multiply(a, b):
    return a * b

print(add(10, 20))
print(multiply(30, 40))