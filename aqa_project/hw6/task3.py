# Напишіть програму, що. вставляє пробіл перед великою літерою
import re

demo_string1 = 'thisIsNewString'
pattern = '[A-Z]'
res = re.findall(pattern, demo_string1)

for el in res:
    demo_string1 = demo_string1.replace(el, " " + el)

print(demo_string1)


