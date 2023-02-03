def find_outlier(integers):
    first = integers[0]
    second = integers[1]
    third = integers[2]
    flag = ''
    if first%2 == 0 and second%2 == 0: #if even and even
        if third%2 == 1:
            return third
        else:
            flag = 'even'
    if first%2 == 1 and second%2 == 1: #if odd and odd
        if third%2 == 1:
            flag = 'odd'
        else:
            return third

    if first%2 == 1 and second%2 == 0: #if odd and odd
        if third%2 == 0:
            return first
        else:
            return second
    if first%2 == 0 and second%2 == 1: #if odd and odd
        if third%2 == 0:
            return second
        else:
            return first
        
    for num in integers:
        if flag == 'even':
            if num%2 == 1:
                return num
        if flag == 'odd':
            if num%2 == 0:
                return num