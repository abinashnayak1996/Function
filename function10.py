# intersection of two array by lambda function
array1 = [1, 2, 3, 5, 7, 8, 9, 10]
array2 = [1, 2, 4, 8, 9]

result = list(filter(lambda x: x in array1, array2))
print (result)