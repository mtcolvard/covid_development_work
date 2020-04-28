import math

# def filter_func(a):
#     lst = sum(int(d) ** (i+1) for i, d in enumerate(str(a))) == a
#     print(lst)

def filter_func(a):
    lst = (int(d) ** (i+1) for i, d in enumerate(str(a)))
    print(lst)

filter_func(10)

# def sum_dig_pow(a, b):
    # return filter(filter_func, range(a, b+1))
