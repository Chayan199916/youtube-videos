''' Topics : List comprehension and Set comprehension with examples '''

# list comprehension

# Basic syntax : [var for var in iterable if var satisfies a condition]

my_string = 'play with python'

res = [letter for letter in my_string if letter not in 'aeiou']

print(res)

# set comprehension

# Basic syntax : {var for var in iterable if var satisfies a condition}

my_string = 'play with python'

res = {letter for letter in my_string if letter not in 'aeiou'}

print(res)