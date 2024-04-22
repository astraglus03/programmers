def solution(my_string):
    answer = []
    a = [int(i) for i in str(my_string) if i.isdigit()]
    return sorted(a)