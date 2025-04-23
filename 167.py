def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    if n % 3 == 0:  
        print ( "chislo delitsya na 3")
    else:
        print ( "chislo ne delitsya na 3")

