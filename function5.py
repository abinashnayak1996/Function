# count lower and upper letter in a string
def count(str):
    upper = 0
    lower = 0
    for i in str:
        if i.isupper():
            upper = upper + 1
        elif i.islower():
            lower = lower + 1
    return upper, lower


print(count('I aM AbiNaSh nAyaK'))
