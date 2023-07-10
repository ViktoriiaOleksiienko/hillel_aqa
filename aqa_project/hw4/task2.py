'''
2.Створіть словник із даними про студентів: ключі - імена студентів, значення - бали для кожного.
Програма повинна визначити середній бал і вивести імена студентів, чий бал вище середнього.
'''

import math
from statistics import mean

students = {'Kate': [5, 2, 4, 5, 5], 'John': [3, 3, 3, 3, 3], 'Mark': [1, 5, 1, 5, 2], 'Mia': [5, 5, 5, 5, 5], 'Emilia': [4, 4, 4, 2, 4], 'Sam': [2, 3, 4, 5, 1]}


def average_score(parameter1):
    return mean(parameter1)


for student in students:
    student_marks = students[student]
    average_student_marks = average_score(student_marks)
    if average_student_marks > 3:
        print(student)


'''additional solution

def get_good_students (student_dictionary):
    name_list = []
    for student in students:
        student_marks = students[student]
        average_student_marks = average_score(student_marks)
        if average_student_marks > 3:
            name_list.append(student)
    return name_list


print(get_good_students(students))
'''