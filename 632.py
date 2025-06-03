array = [1,4,1,6,"hello","a",5,"hello","hello"]
for i in range (0,len(array)):
    for j in range (i + 2 , len(array)):
        if array[j] == array[i]:
           print (array[j])
           print (array[i])
