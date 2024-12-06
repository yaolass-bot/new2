

x = int(input("Povtorenie:"))
p = int(input("CHISLO POVTORENIY:"))
y = int(input("nujnaya summa vklada"))

t = 0 # KOLICHESTVO LET VKLADA
n = 0 # TEKUSHAYA SUMMA VVKLADA
while (n < y):
    n = x + n * p/100 * (t)
    t = t + 1
    print(t)
    print(n)