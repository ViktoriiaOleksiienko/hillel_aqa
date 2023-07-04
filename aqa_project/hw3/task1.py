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
