'''Створіть за допомогою list comprehension список, в якому буде 100 елементів, і кожен із яких буде в границях
 від 1 до 10(для цього можна скористатись функцією randint із модуля random). Порахуйте кількість кожного елемента
і виведіть в консоль'''

import random

my_list = [random.randint(1, 10) for x in range(100)]
element_counts = {i: my_list.count(i) for i in range(1, 11)}

for element, count in element_counts.items():
    print(f"Element {element}: {count} times")