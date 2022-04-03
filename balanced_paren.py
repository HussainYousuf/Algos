def isbalanced(string):
    stack = []
    for i, c in enumerate(string):
        if(c in ['(']):
            stack.append(i)
        if(c in [')']):
            try:
                stack.pop()
            except:
                return (False, i)
    if(stack):
        return (False, stack.pop())
    else:
        return True

print(isbalanced(")()("))