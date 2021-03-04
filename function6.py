# find out even number from a list
def is_even_num(l1):
    l2 = []
    for n in l1:
        if n % 2 == 0:
            l2.append(n)
    return l2


print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))
