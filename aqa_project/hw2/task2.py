'''
В змінній birth_month запишіть номер місяця вашого народження (дані введіть з консолі). В залежності від введених даних виведіть характеристику для відповідної пори року:
Зима - За вікном падав сніг.
Весна - Все довкола розцвітало.
Літо - Діти насолоджувались літніми канікулами.
Осінь - Все довкола загоралось яскравими фарбами.
'''

birth_month = int(input('Введіть номер місяця вашого народження'))
if birth_month == 1 or birth_month == 2 or birth_month == 12:
    print('Зима - За вікном падав сніг')
elif birth_month >=3 and birth_month <= 5:
    print('Весна - Все довкола розцвітало')
elif birth_month >= 6 and birth_month <=8:
    print('Літо - Діти насолоджувались літніми канікулами')
elif birth_month >= 9 and birth_month <= 11:
    print('Осінь - Все довкола загоралось яскравими фарбами')
else:
    print('Введіть валідний номер місяця вашого народження: значення має бути від 1 до 12')