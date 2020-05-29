''' Topics : sequence, iterator, iterable, differences between them  with code snippets'''
import math
my_list = [1, 2, 3, 4, 5] # list / iterable

print(hasattr(my_list, '__iter__'))
print(hasattr(my_list, '__next__'))

for ele in my_list:
    print(ele)

my_iter = iter(my_list) # my_list.__iter__()

while True:
    try:
        print(next(my_iter)) # my_list.__next__()
    except StopIteration:
        print('We have reached end of the list')
        break

class my_own_iterator:
    """Class about an iterator which performs i ** i for all i <= user_input"""

    def __init__(self, max = 0):
        self.max_ele = max
    
    def __iter__(self):
        self.ele = 1
        return self

    def __next__(self):
        if self.ele <= self.max_ele:
            result = self.ele ** self.ele
            self.ele += 1
            return result
        else:
            raise StopIteration

my_itr_obj = my_own_iterator(5)

my_itr = iter(my_itr_obj)

# print(next(my_itr))
# print(next(my_itr))
# print(next(my_itr))
# print(next(my_itr))
# print(next(my_itr))
# print(next(my_itr))

while True:
    try:
       print(next(my_itr))
    except StopIteration:
        print('We have reached the limit...')
        break

