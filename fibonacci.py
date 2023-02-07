def fibonacci(the_number):
    if the_number == 0:
        return 0
    if the_number == 1 or the_number == 2:
        return 1
    return fibonacci(the_number -1 ) + fibonacci(the_number - 2)


print(fibonacci(3))
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(5))
print(fibonacci(8))
print(fibonacci(31))