import re
'''
Напишіть програму, що видаляє область дужок в стрічці
["example (.com)", "github (.com)", "stackoverflow (.com)"] ->
example
github
stackoverflow
'''

demo_list1 = ['example (.com)', 'github (.com)', 'stackoverflow (.com)', 'test(test)']
pattern = '\([^()]*\)'
for el in demo_list1:
    res = re.sub(pattern, '', el)
    print(res)
