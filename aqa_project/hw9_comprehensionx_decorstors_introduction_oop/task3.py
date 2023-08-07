'''Створіть декоратор, який виводить в консоль ім'я функції, яку було викликано. Наприклад, створіть пару функцій для
аріфметичних операцій додавання і множення. При виклику цих функцій має повертатись результат операції і виводиться в
консоль ім'я функції, яку було викликано.'''


def log_function_name(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' was called.")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_function_name
def add(a, b):
    return a + b

@log_function_name
def multiply(a, b):
    return a * b


result_add = add(10, 20)
result_multiply = multiply(10, 20)

print("Result of add:", result_add)
print("Result of multiply:", result_multiply)