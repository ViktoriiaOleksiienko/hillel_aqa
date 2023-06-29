#В змінній minute лежить число от 0 до 59, згенероване випадковим чином. Визначте в якій четверті години попадає це число (в першій, другій, третій чи четвертій)

import random
minute = random.randint(0, 59)
print(minute)
if minute <= 15:
    print ('the first quarter of an hour')
elif minute > 15 and minute <= 30:
    print('the second quarter of an hour')
elif minute > 30 and minute <= 45:
    print('the third quarter of an hour')
else:
    print('fourth quarter of an hour')


