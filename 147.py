def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

number = 122
print(sum_of_digits(number))

if sum_of_digits(number) % 3 == 0:

     print ("chislo delitsya na 3")
else:
     print("chislo ne delitsya na 3")
