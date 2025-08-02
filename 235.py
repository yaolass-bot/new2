
array = [ 2, 6,7,8,9,8,1,7,5]
start_index = array[0]
end_index = array[8]
max_value = array[start_index]
min_value = array[end_index]
for i in range(start_index, end_index):
    if array[i] > max_value:
            max_value = array[i]
            print(max_value)
