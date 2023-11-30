def name_in_str(strng : str, name : str) -> bool:
    
    stack = list(name.lower())[::-1]
    
    for char in strng.lower():
        if stack == []:
            break
        else:
            if char == stack[-1]:
                stack.pop()
        print(stack)

    if stack == []:
        return True
    else:
        return False