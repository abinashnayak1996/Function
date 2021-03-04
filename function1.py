# calculate maximum number
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


print(max_of_three(9, 11, 8))
