'''
Написати функцію, яка отримує у вигляді параметра ім'я файлу (names.txt) і повертає список усіх прізвищ з нього.
Кожен рядок файлу містить номер, прізвище, країну. Файл створити власноруч і записати туди дані
'''


def get_last_names(file_name):
    last_names = []

    with open(file_name, 'r') as file:
        for line in file:
            parts = line.split()
            last_name = parts[1]
            last_names.append(last_name)
    return last_names


file_name = "names.txt"
last_names_list = get_last_names(file_name)
print(last_names_list)