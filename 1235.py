array = [ 2, 6,7,8,9]
array1 =[]
max = array[0]
for i in range(len(array)):
    if array[i] > max:
            max = array[i]
array1.append(array[i])
print(array1)