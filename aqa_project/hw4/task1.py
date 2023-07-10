'''Для всіх трьох задач скористайтесь написанням функцій. В межах розумного робіть функції невеликими за розміром і перевикористовуйте код.
1.Дано два списки чисел. Знайдіть всі числа, що зустрічаються як в першому, так і другому списках, і надрукуйте їх у порядку зростання.
'''
first_list = [1, 6, 4, 33, 2]
second_list = [2, 1, 55, 4, 100]


def same_values(list1, list2):
    crossed_list = list(set(list1) & set(list2))
    crossed_list.sort()
    return crossed_list


print(same_values(first_list, second_list))