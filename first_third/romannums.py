def to_roman(arabicNum):
    output = []
    numeralMap = {
        "M":1000,
        "CM":900,
        "D":500,
        "CD":400,
        "C":100,
        "XC":90,
        "L":50,
        "XL":40,
        "X":10,
        "IX":9,
        "V":5,
        "IV":4,
        "I": 1
    }
    for i in numeralMap.keys():
        evenTimes = arabicNum//numeralMap[i]
        arabicNum -= evenTimes * numeralMap[i]
        for j in range(evenTimes):
            output.append(i)
    return ''.join(output)


print(to_roman(4))
print(to_roman(944))
print(to_roman(150))
print(to_roman(205))
print(to_roman(847))
print(to_roman(999))
print(to_roman(2999))