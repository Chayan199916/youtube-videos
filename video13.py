'''                         Topics : Anonymous function , Lambda expression                          '''
# Points of discussion :

# 1. What is it ?
# 2. Syntax 
# 3. Example
# 4. Use

# def function_name(arg):
#     statements
#     return result

# lambda args : single_exp 

my_date = '12/12/2012'

my_result = my_date.split('/')

def my_func(str, dele):
    return str.split(dele)

print(my_func('12/12/2012', '/'))

my_func = lambda str, dele : str.split(dele)

print(my_func('12/12/2012', '/'))

def attach(name):
    return lambda prefix : prefix + name

tot_name = attach('ALie')

print(tot_name('Dr.'))