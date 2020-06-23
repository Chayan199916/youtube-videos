'''                       Filter function in python                                                        '''



# Topics :

# 1. Purpose of filter function 
# 2. Syntax
# 3. Example
# 4. How to use lambda expression inside the filter function
# 5. Diff between map and filter
# 6. Bonus point : What will happen,
#                  if we don't pass any function in the list of 
#                  arguments

# Syntax of filter function

# Filter Syntax : filter(function, iterable) 
#                 returns filter object                                                      
#                 / iterator

# Map Syntax : map(function, iterable) # returns map object / iterator
# lambda expression : lambda args : exp if condition is true 
#                                               else expression

# solution using for loop :

# for element in iterable:
#     if condition is True for the element:
#         return True
#     else:
#         return False

# mapping from other type to boolean:

# any string : True
# any number except 0 : True
# None : False


# Purpose of filter function :

# Solution using for loop :

def extract_evens(list_no):
    for ele in list_no:
        if ele % 2 == 0:
            print(ele)

extract_evens(range(10)) # returns all evens 

# SOlution using filter function 

# my_list = range(10)

def checK_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

my_result = list(filter(checK_even, my_list))
print(my_result)

for ele in my_result:
    print(ele)


my_string = 'play with python'

# my_result = ['p', 'l', 'a', ]

def extract(letter):
    if letter in 'aeiou':
        return True
    else:
        return False 

my_result_obj = filter(extract, my_string)
my_result_list = list(filter(extract, my_string))
my_result_set = set(filter(extract, my_string))

print(my_result_list)
print(my_result_set)
print(my_result_obj)

# lambda expression inside the filter function

my_string = 'play with python'

my_result_obj = list(filter(lambda letter : True if letter in 'aeiou' else False, my_string))

print(my_result_obj)

# Difference between map function and filter function

my_string = 'play with python'

my_result_list1 = list(map(lambda letter : letter if letter in 'aeiou' else None, my_string))
my_result_list2 = list(filter(lambda letter : letter if letter in 'aeiou' else None, my_string))

print(my_result_list1)
print(my_result_list2)

if None:
    print("worKing")
else:
    print('not worKing')

# Bonus part :

my_exp_list = [1, 2, 3, 4, 0, 'a', 'w', None, None]

my_result = list(filter(None, my_exp_list))

print(my_result)