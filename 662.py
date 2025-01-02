import math


def heron_area(a,b,c):
   s = (a + b + c)/2
   return math.sqrt(s*(s-a)*(s-b)*(s-c))
a = 3
b = 3
c = 5
print(heron_area(a,b,c))















































