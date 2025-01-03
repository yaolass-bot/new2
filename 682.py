from functools import  cmp_to_key

def largest_number(nums):
   nums = list(map(str, nums))

def compare (x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

    nums.sort(key=cmp_to_key(compare))

    largest_num = ''.join(nums)

    if largest_num [0] == '0':
        return '0'

    return largest_num

numbers = [56, 9, 11, 2]

print(largest_number(numbers))
















































