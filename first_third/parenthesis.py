def check(myStr):
    stack = []
    for i in myStr:
        if i in myStr:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    return len(stack) == 0

print(check('()()'))