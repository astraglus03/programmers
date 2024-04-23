def solution(numbers, direction):
    answer = []
    a=len(numbers)
    if(direction == 'right'):
        s= numbers.pop()
        numbers.insert(0,s)
    if(direction == 'left'):
        ss=numbers.pop(0)
        numbers.append(ss)
    return numbers