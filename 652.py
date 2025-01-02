def find_max_element(matrix):
    max_element = float('-inf')
    for row in matrix:
        for element in row:
            if element > max_element:
                max_element = element
    return max_element
matrix =[
     [9,70,20,67,33],
     [60,20,94,14,77],
     [27, 8,45,0,13],
     [39,47,25,97,69],
    [83,13,100,1,85]
]
max_element = find_max_element(matrix)
print("The maximum element in matrix is:", max_element)





