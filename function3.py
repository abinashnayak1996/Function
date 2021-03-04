# reverse a string by using function
def string_reverse(str):
    reverse = ''
    index = len(str) - 1
    while index >= 0:
        reverse = reverse + str[index]
        index = index - 1
    return reverse


print(string_reverse('abinash'))
