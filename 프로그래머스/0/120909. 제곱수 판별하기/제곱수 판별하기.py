def solution(n):
    answer = 0
    if((n**0.5).is_integer()):
        answer=1
    else:
        answer=2
    return answer