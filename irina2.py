v = int(input("Введите скорость в км/ч:"))
t = int(input("Введите время в ч:"))
if(t * v % 109 == 0):
       print ( 109 )
else:
    y = t * v % 109
print(y)