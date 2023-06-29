'''
Напишіть програму, в яку спочатку запишіть в 1 змінну ваше ім'я, в 2 ваше прізвище, а потім виводить на екран повідомлення з вашими особистими даними.
Тут використайте конкатенацію, тобто об'єднайте стрічки.
Виведіть результат в нижньому, верхнього регістрах з капіталізацією перших букв кожного слова.
Змініть значення своєї змінної, яку ви створили на кроці 1 , додавши до свого імені декілька пробілів на початку та вкінці.
Прослідкуйте щоб \t \n зустрічались хоча б один раз. Виведіть нове значення. Видаліть пропуски і збережіть новий результат.
'''

first_name = "Viktoriia"
second_name = "Oleksiienko"
full_name = first_name + ' ' + second_name
print(full_name)

print(full_name.lower())
print(full_name.upper())
print(first_name.capitalize() + ' ' + second_name.capitalize())

first_name = "   Viktoriia"
second_name = "Oleksiienko   "
print('\tViktoriia')
print('Viktoriia\nOleksiienko')
print(full_name.strip())