

a = int(input("Введите A"))
b = int(input("Введите B"))
c = int(input("Введите C"))

if (a == b == c):
   print(3)
elif (a == b or b == c or a == c):
    print(2)
else:
   print (0)
