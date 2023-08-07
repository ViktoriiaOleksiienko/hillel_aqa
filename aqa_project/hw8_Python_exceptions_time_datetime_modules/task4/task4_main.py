'''Реалізуйте функцію, яка вираховує ваш точний вік(не обов'язково вказувати свої данні), вираховуючі різницю між
наданим значеням і значенням datetime.now(). Приймає дату та час(datetime), повертає два значення:
datetime і datetime.timestamp. В цій задачі скористайтесь для конвертації datetime.timestamp. Виведіть результат в консоль'''

from datetime import datetime


def age_now(birth_date):
    if not isinstance(birth_date, datetime):
        raise ValueError("birth_date must be a datetime object")
    current_date = datetime.now()
    age_timedelta = current_date - birth_date
    age_years = age_timedelta.days // 365

    return age_timedelta, age_years


birth_date = datetime(1999, 10, 8)
age_timedelta, age_years = age_now(birth_date)

print("Given date:", birth_date)
print("Date difference in days:", age_timedelta)
print("Age in years:", age_years)
print("Age in seconds:", age_timedelta.total_seconds())
