# task 1
# def square(x):
#         return x*x
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_num = list(map(square, numbers))
# print(new_num)

# task 2
# num = [1,2,3]
# print(sum(num))

# task 3
# print(all([1, 2, 3, 0, -1]))
# print(all([1, 2, 3]))

# task 4
# print(any([1, 2, 3, 0, -1]))
# print(any([1, 2, 3]))

# task 5
# num = [1, 2, 3, 0, -1]
# neg = list(filter(lambda x: (x < 0), num))
# print(neg)

# task 6
# list_ = [1, 2, 3, 0, -1]
# even_num = len(list(filter(lambda x: (x % 2 == 0), list_)))
# print(even_num)

# task 7
# wrd = ['hello', 'world', 'incapsulation', 'inheritance']
# filt_wrd = list(filter(lambda x: len (x) > 6, wrd))
# print(filt_wrd)

# task 8
# from functools import reduce
# seq = [1, 2, 3, 4]
# multiply = reduce(lambda a, b: a*b, seq)
# print(multiply)

# task 9
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# odd_num = len(list(filter(lambda x: (x % 2 != 0), list_)))
# even_num = len(list(filter(lambda x: (x % 2 == 0), list_)))
# print('Количество нечетных чисел: ', odd_num)
# print('Количество четных чисел: ', even_num)

# task 10
# num = [-1, 2, 3, 4, -5, 6, 7, -8, 9]
# pos = list(filter(lambda x: (x > 0), num))
# neg = list(filter(lambda x: (x < 0), num))
# print('Положительны: ', pos)
# print('Отрицательные: ', neg)


# task 11
# nums = [-1, 2, 3, 4, -5, 6, 7, -8, 9, 0]
# pos_neg = list(map(lambda x:-1 if x < 0  else 1 if x > 0 else 0, nums ))
# print(pos_neg)

# task 12
# num = input()
# n = (num[2:] + num[:2])
# print(n)

# task 13
# def reverseArray(a):
#     return a[::-1]

# task 14
# def isBalanced(s):
#     balance = []
#     brackets = {'{':'}', '(':')', '[':']'}
#     for i in s:
#         if i in ['{', '(', '[']:
#             balance.append(i)
#         else:
#             if balance:
#                 top = balance.pop()
#                 if brackets[top] != i:
#                     return 'NO'
#             else:
#                 return 'NO'
#     return 'NO' if balance else 'YES'

