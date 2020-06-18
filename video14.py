'''                                     Map in python                                               '''
# Topics : 
# 1. What is map?
# 2. Basic syntax of map
# 3. Examples
# 4. lambda expression with map

# Basic syntax of map :   list(map(function, iterable)) #returns map object

# Basic syntax of lambda expression : lambda args : expression if condition is true else expression 


# Example :

my_string = 'play with python'

# my_result = ['p', 'l', 'a', ]

def extract(letter):
    if letter in 'aeiou':
        return letter 

my_result_obj = map(extract, my_string)
my_result_list = list(map(extract, my_string))
my_result_set = set(map(extract, my_string))

# print(my_result_list)
# print(my_result_set)
# print(my_result_obj)

my_result_obj = map(lambda letter : letter if letter in 'aeiou' else None, my_string)
my_result_list = list(map(lambda letter : letter if letter in 'aeiou' else None, my_string))
my_result_set = set(map(lambda letter : letter if letter in 'aeiou' else None, my_string))

# print(my_result_list)
# print(my_result_set)
# print(my_result_obj)

my_numbers1 = [1, 2, 3]
my_numbers2 = [4, 5, 6]

my_result_final = list(map(lambda first, second : first ** second, my_numbers1, my_numbers2))

print(my_result_final)