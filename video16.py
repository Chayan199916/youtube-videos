'''                                                 reduce function in python                                   '''

# Topics: 

# 1. Purpose
# 2. Syntax
# 3. Example
# 4. Using lambda expression inside reduce function
# 5. Diff between map, filter and reduce



from functools import reduce # python 3, in python 2 was in __builtin__

# syntax

# reduce(function, iterable, initializer) -> syntax

# def sum(num1, num2):

#     return num1 + num2

# example

# result = reduce(lambda num1, num2 : num1 + num2, range(5), 5)
# print(result)

# ((((0 + 1) + 2) + 3) + 4) -> internal working if initializer not provided
# (((((0 + 5) + 1) + 2) + 3) + 4) -> internal working if initializer provided

# def my_reduce(function_name, my_iterable, initializer = None):

#     my_iter = iter(my_iterable)

#     if initializer:

#         result = initializer

#     else:

#         result = next(my_iter)

#     for ele in my_iterable:

#         result = function_name(result, next(my_iter))

#     return result

# print(my_reduce(sum, range(5), 5))

# lambda expression inside reduce

# result = reduce(lambda num1, num2 : num1 + num2, range(5), 5)

# print(result)