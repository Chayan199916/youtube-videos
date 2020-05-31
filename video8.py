'''                 Topics : generator, generator expression, generator function, 
                            advantages of generator over list                                               '''

# what is generator ?

class my_own_iterator:
    """Class about an iterator which performs i ** i for all i <= user_input"""

    def __init__(self, max = 0):
        self.max = max
    
    def __iter__(self):
        self.ele = 1
        return self

    def __next__(self):
        if self.ele <= self.max:
            result = self.ele ** self.ele
            self.ele += 1
            return result
        else:
            raise StopIteration


my_itr_obj = my_own_iterator(5)

my_itr = iter(my_itr_obj)

# for ele in my_itr:
#     print(ele)


# generator expression / generator comprehension 

my_gen = (i ** i for i in range(6) if i > 0)

for ele in my_gen:
    print(ele)

# Basic syntax : (expression for var in iterable if var satisfies a condition)

# generator function

def my_gen_fun(max = 0):
    num = 1
    while num <= max:
        yield num ** num
        num += 1

my_gen_obj = my_gen_fun(5)

print(my_gen_obj)

for ele in my_gen_obj:
    print(ele)

def my_special_gen():
    num = 1
    while True:
        yield num
        num += 1

# for ele in my_special_gen():
#     print(ele)

# iter(callable, sentinel= some_val)

my_inf_seq = (ele for ele in iter(int, 1))

for ele in my_inf_seq:
    print(ele)




    


 

