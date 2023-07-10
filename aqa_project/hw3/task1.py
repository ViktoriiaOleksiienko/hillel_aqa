'''
Написати програму, для введення та перегляду нотаток. Програма пропонує користувачу вводити ключові слова, та опрацьовує їх. Перелік ключових слів:

add - додати нотатку. Користувач вводить текст нотатки, який зберігається у програмі та є дійсним до її завершення
earliest - виводить збережені нотатки у хронологічному порядку - від найстарішої до найновішої
latest - виводить збережені нотатки у хронологічному порядку - від найновішої до найстарішої
longest - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої
shortest - виводить збережені нотатки у порядку їх довжини - від найкоротшої до найдовшої
Exit - вихід
'''

list_of_notes = []
while True:
    word = input('Введіть одне з ключових слів, щоб працювати з нотатками (add, earliest, latest, longest, shortest, exit): ')
    if word == 'add':
        add_note = input('Введіть нотатку: ')
        list_of_notes.append(add_note)
        print(list_of_notes)
    if word == 'earliest':
        print('Від найновішої до найпізнішої:' + str(list_of_notes))
    if word == 'latest':
        list_of_notes.reverse()
        print('Від найпізнішої до найновішої:' + str(list_of_notes))
    if word == 'longest':
        list_of_notes.sort(key=len, reverse=True)
        print('Від найдовшої до найкоротшої:' + str(list_of_notes))
    if word == 'shortest':
        list_of_notes.sort(key=len)
        print('Від найкоротшої до найдовшої:' + str(list_of_notes))
    if word == 'exit':
        break