def solution(my_string):
    s = []
    for ch in my_string:
        if ch not in s:
            s.append(ch)
    return ''.join(s)