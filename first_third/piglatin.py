def pig(string):
    answer = string.split(" ")
    for i in range(len(answer)):
         answer[i] = answer[i][1:] + answer[i][0]
    second = map(lambda x : x + 'ay ', answer)
    return ''.join(second)


print(pig('rootbeer'))
print(pig('apple university'))
print(pig('this is pig latin'))
