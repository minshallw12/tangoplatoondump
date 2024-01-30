
num = 154554

def digit_check(n):
    my_dict = {}

    while n > 0:
        print(n)
        digit = n % 10

        if digit not in my_dict:
            my_dict[digit] = 1
        else:
            my_dict[digit] += 1

        n = n // 10
    return my_dict

print(digit_check(num))