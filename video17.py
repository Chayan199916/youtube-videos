'''                             Decorators in python                                    '''
#   Part -1
''' subtopics : 

 1. What is Decorator?
 2. Diff kinds 
 3. Use
 4. Examples

-------------------------------------------- 
* Metaprogramming is a concept which talks about modifying a part of the program from another part at compile time.
-------------------------------------------- '''

# Prerequisites
# --------------------------

# what is callable?

# def demo_callable_func(): 

# 	return 0

# num = 5
# demo_callable_func.__call__()
# class demo_callable_class: 

#     def __call__(self): 

#         print('Do something...')

# 	# def do_something():

# 	# 	print('Do something...') 

# print(callable(demo_callable_func)) # returns True
# print(demo_callable_func.__call__()) # similar to demo_callable_func()
# print(callable(num)) # returns False
# print(callable(demo_callable_class)) # returns True
# demo_callable_class_obj = demo_callable_class()
# demo_callable_class_obj.__call__()

'''

So the sequence of execution is like this:

demo_callable_class is object of type class so when we do like demo_callable_class(), 
it is nothing but demo_callable_class.__call__() inside __call__() of type class, 
it first calls __new__() which allocates memory(an empty object) and 
then calls __init__() to initialize it and at last the object is returned.

'''

# Functions are objects, names are identifiers bound to those objects---------

# demo_callable_func_copy = demo_callable_func # diff names can be bound to one function object
# print(demo_callable_func_copy())

# Functions can be passed as arguments-----------

# def demo_main_function(arg_function_1, arg_function_2, check_var): # higher order function

# 	if check_var:

# 		arg_function_1()

# 	else:

# 		arg_function_2()

# demo_main_function(lambda : print("Inside first argument function"), 
# 				   lambda : print("Inside second argument function"), False)

# Functions can be defined inside another function and returned from that function----------

# def demo_parent(check_var):

#     def first_child_function():
#         return "Inside first child function"

#     def second_child_function():
#         return "Inside second child function"

#     if check_var:
#         return first_child_function
#     else:
#         return second_child_function

# demo_parent_result = demo_parent(False)
# print(demo_parent_result())

# Closures in python-------

'''
non local variable (to make the read only variable writable using nonlocal keyword)
nested function

'''
def demo_parent_function(msg):
	''''outer function'''

	def demo_nested_function():
		'''nested function'''
        # nonlocal msg = "modified"
		print(msg)
	
	demo_nested_function()
	return demo_nested_function

demo_parent_function_cp =  demo_parent_function('hello world')
demo_parent_function_cp()
del demo_parent_function
demo_parent_function_cp()
print(demo_parent_function_cp.__closure__[0].cell_contents)