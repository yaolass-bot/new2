def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

total = 122
print(sum_of_digits(total))

if sum_of_digits(total) % 3 == 0:

     print ("chislo delitsya na 3")
else:
     print("chislo ne delitsya na 3")
