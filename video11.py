
'''                               timeit module                                                                          '''
import timeit

# print(timeit.timeit(stmt='''num = 5''', number= 10000))

# first way

# basic syntax : timeit.timeit(setup = some_code, stmt = some_code, number = no_iteration)

#second way

# def test_function():
#     test_codes

#basic syntax : timeit.timeit('f()', 'from __main__ import test_function as f', number=no_iteration)


def list_comp():
    return [ele for ele in range(1000)]

def generator_comp():
    return (ele for ele in range(1000))

print(timeit.timeit('f()', 'from __main__ import list_comp as f', number=1000))
print(timeit.timeit('f()', 'from __main__ import generator_comp as f', number=1000))

print(timeit.repeat('f()', 'from __main__ import list_comp as f',repeat=4, number=1000))