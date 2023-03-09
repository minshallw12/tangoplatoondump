def bottles(num):
    i = num
    while i > 1:
        print(f'{i} bottles of beer on the wall, {i} bottles of beer');
        print(f'Take one down and pass it around, {i-1} bottles of beer on the wall.');
        i -= 1
    while i == 1:    
        print('1 bottle of beer on the wall, 1 bottle of beer.')
        print('Take one down and pass it around, no more bottles of beer on the wall.')
        i -= 1
    if i <= 0:
        print('No more bottles of beer on the wall, no more bottles of beer.')
        return f'Go to the store and buy some more, {num} bottles of beer on the wall.'
    

#print(bottles(99))
#print(bottles(1))
#print(bottles(0))