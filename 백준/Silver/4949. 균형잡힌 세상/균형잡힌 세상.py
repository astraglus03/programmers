while True:
    a = input()
    if a == '.':
        break
    res = []
    for i in a:
        if i == '(' or i == '[':
            res.append(i)
        if i == ')':
            if len(res) != 0 and res[-1] == '(':
                res.pop()
            else:
                res.append(')')
                break
        if i == ']':
            if len(res) != 0 and res[-1] == '[':
                res.pop()
            else:
                res.append(']')
                break

    if len(res) == 0:
        print('yes')
    else:
        print('no')