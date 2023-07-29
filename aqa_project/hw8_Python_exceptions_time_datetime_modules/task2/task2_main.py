def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error. Division by zero is impossible:("


print(divide(10, 0))
print(divide(8, 2))
print(divide(15, 1))
