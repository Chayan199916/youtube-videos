'''                         pros and cons of comprehension                                          '''

my_string = 'play with python'

res = []

for letter in my_string:
    if letter in 'aeiou':
        res.append(letter)

print(res)

# res = [letter for letter in my_string if letter in 'aeiou']

my_exp_iter = range(1000)

def loop():
    res = []
    for ele in my_exp_iter:
        res.append(ele)
    return res

def comp():
    return [ele for ele in my_exp_iter]

import timeit

# print(timeit.timeit('f()', 'from __main__ import loop as f', number= 1000))
# print(timeit.timeit('f()', 'from __main__ import comp as f', number= 1000))

my_matrix = [
    [1, 2, 3], 
    [4, 5, 6]
]

flattened_matrix = [ele for row in my_matrix for ele in row ]

print(flattened_matrix)