

x = int(input("Summa vklada:"))
p = int(input("Procenty po vkladu:"))
y = int(input("Nujnaya summa vklada"))

t = 0 # Kolichestvo let vklada
n = 0 # Tekushaya summa vklada
while (n < y):
    n = x + n * p/100 * (t)
    t = t + 1
    print(t)
    print(n)
