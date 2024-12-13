array = [1,4,1,6, "hello","a",5,"hello"]
for i in range (0,len(array)):
    c = 0
    for j in range (i + 1, len(array)):
       if j == i + 1:
           c += 1
           print (array[j])
           if c == 0:
            print (array[i])



























