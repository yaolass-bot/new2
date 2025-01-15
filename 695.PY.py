def areaTriangle (a,b,c):
    s = (a*b*c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5
a = 2
b = 3
c = 4
print(areaTriangle(a,b,c))


