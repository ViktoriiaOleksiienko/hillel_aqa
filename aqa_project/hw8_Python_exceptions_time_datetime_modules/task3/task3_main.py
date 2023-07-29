from datetime import datetime, timedelta

def add_or_subtract_days_from_date(input_date, days, add=True):
    if not isinstance(input_date, datetime):
        raise ValueError("input_date must be a datetime object")
    if not isinstance(days, int):
        raise ValueError("days must be an integer")

    delta = timedelta(days=days)

    if add:
        result_date = input_date + delta
    else:
        result_date = input_date - delta

    return result_date


input_date = datetime(2023, 7, 29, 16, 30, 55)
days_to_add = 2
days_to_subtract = 20

new_date_after_addition = add_or_subtract_days_from_date(input_date, days_to_add)
new_date_after_subtraction = add_or_subtract_days_from_date(input_date, days_to_subtract, add=False)

print("Given date:", input_date)
print("New date (+2 days):", new_date_after_addition)
print("New date (-20 days):", new_date_after_subtraction)