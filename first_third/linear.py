def basic_linear(str, str2):
    lst2 = []
    for i in range(len(str2)):
        if str == str2[i]:
            return i


print(basic_linear("a", "banana"))

def globalLinear(str, str2):
    data = []
    for i in range(len(str2)):
        if str == str2[i]:
            data.append(i)
    return data
print(basic_linear("a", "banana"))
print(globalLinear('n', 'banana'))
print(globalLinear('5', '15845321565184'))
print(globalLinear(' ', "How you doin'?"))