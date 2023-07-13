#Напишіть програму на Python, щоб перевірити, чи є заданий рядок числом, за допомогою лямбда

given_string = 'Is this an int?'

this_is_string = lambda a: a.isnumeric()
print(this_is_string(given_string))
