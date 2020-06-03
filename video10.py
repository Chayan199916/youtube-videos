'''                                     getsizeof in python                                                '''
import sys
num = 5 

# print(num.__sizeof__())
# print(sys.getsizeof(num))

lis = [1, 2, 3, 4] 

# print(lis.__sizeof__())
# print(sys.getsizeof(lis))

# print(sys.getsizeof(lis) + len(lis) * int().__sizeof__())

lis1 = [ele for ele in range(1000)]
gen1 = (ele for ele in range(1000))

print(lis1.__sizeof__() + len(lis1) * int().__sizeof__())
print(gen1.__sizeof__())


