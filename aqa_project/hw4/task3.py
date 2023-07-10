'''
3.Створіть списки із значеннями для name, surname, location, наприклад name = ['Alex', 'John', 'Simba']. напишіть програму,
яка створює словники з даними випадкових людей на основі ваших списків, роздрукуйте результат.
для випадковості значень скористайтесь модулем random. приклад згенерованого словника:
{'name':'Liza', 'surname':'Djoconda', 'location':'Florence'}
'''

import random

name = ['Kate', 'Samanta', 'Emilia', 'Kristina', 'Liana']
surname = ['Jonson', 'Wolter', 'Martin', 'Jobs', 'Brown']
location = ['California', 'NY', 'LA', 'London', 'Paris']


def dictionary_creating(parameter1, parameter2, parameter3):
    random_dictionary = {'name': random.choice(parameter1), 'surname': random.choice(parameter2), 'location': random.choice(parameter3)}
    return random_dictionary


print(dictionary_creating(name, surname, location))
