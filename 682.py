from functools import  cmp_to_key

def compare (x, y):
    return int(str(y) + str(x)) - int(str(x) + str(y))
def from_largest_number(arr):
    str_arr = [str(num) for num in arr]

    str_arr.sort(key=cmp_to_key(compare))

    return '' .join(str_arr)

arr = [56,9,11,2]
result = from_largest_number(arr)
print(result)





















































