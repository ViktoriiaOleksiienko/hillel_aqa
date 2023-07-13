#Напишіть програму на Python для знаходження перетину двох заданих масивів за допомогою лямбда.

first_array = [1, 2, 3, 4, 5]
second_array = [6, 3, 8, 5, 10]

array_crossing = lambda a, b: list(set(a) & set(b))
print(array_crossing(first_array, second_array))
