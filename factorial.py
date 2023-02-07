def factorial(number):
    if number < 1:
        return 'bad input'
    if number == 1:
        return 1
    return number * factorial(number - 1)

print(factorial(4))
print(factorial(7))
print(factorial(8))
print(factorial(1))
print(factorial(0))