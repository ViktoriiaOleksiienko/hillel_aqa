'''
Написати функцію, яка отримує у вигляді параметра ім'я файлу назви інтернет доменів (domains.txt) та повертає їх у вигляді списку рядків (назви повертати без крапки).
'''


def read_domains(file_name):
    with open(file_name, 'r') as file:
        domains = [line.strip().lstrip('.') for line in file.readlines()]
    return domains


file_name = 'domains.txt'
domain_list = read_domains(file_name)
print(domain_list)