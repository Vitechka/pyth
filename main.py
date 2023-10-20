def print_hi(a):
    print("Vik" * a)


print_hi(4)

import random


def storm():
    a = [random.randint(10, 100)]
    for i in a:
        b = i // 2
    return b


print(storm())
