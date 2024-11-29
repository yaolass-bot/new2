x = int(input("summa vklada cv rublyax:"))
p = int(input("procent po vkladu:"))
y = int(input("nujnaya summa vklada:"))

t = 0 #kolichestvo let vklada
n = 0 #tekushaya summa vklada
while ( n < y):
     n = x + p * x
     t = t + 1
     print(t)
