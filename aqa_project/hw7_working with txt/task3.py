'''
Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) і повертає список словників виду
{"date": date} у яких date - це дата з рядка (якщо є), Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]
'''


import re


def find_dates_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    pattern1 = r'(\b\d+(?:st|nd|rd|th)? (?:January|February|March|April|May|June|July|August|September|October|November|December) \d{4}\b)'
    dates_found = re.findall(pattern1, content)
    result = [{"date": date} for date in dates_found]
    return result


file_name = "authors.txt"
dates_list = find_dates_from_file(file_name)
print(dates_list)
