# find out even ,odd number from a given list by using lambda
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x%2 == 0, number))
print(even)
odd_nums = list(filter(lambda x: x%2 != 0, number))
print(odd_nums)