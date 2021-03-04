# using function calculate sum in a list
def sum(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total


numbers = [3, 6, 1, 2, 9]
print(sum(numbers))
