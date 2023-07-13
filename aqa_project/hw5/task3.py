#Напишіть програму на Python, щоб знайти список із максимальною та мінімальною довжиною за допомогою лямбда.
from functools import reduce

short_list = [1]
first_medium_list = ['Hello my friend. How are you?', 'I am fine. And how are you?']
second_medium_list = [1, 2, 3]
long_list = ['hello', 'hi', 'good day', 'gm', 'good evening', 1, 2, 3]

all_lists = [short_list, first_medium_list, second_medium_list, long_list]

max_len_list = reduce(lambda a, b : a if (len(a)>len(b)) else b, all_lists)
min_len_list = reduce(lambda a, b : a if (len(a)<len(b)) else b, all_lists)

print("List with maximum length:", max_len_list)
print("List with minimum length:", min_len_list)


