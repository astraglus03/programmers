def solution(numbers):
    answer = numbers[0]*numbers[1]
    n = len(numbers)  
    for i in range(n):
        for j in range(i + 1, n):
            a = numbers[i] * numbers[j]
            print(a)
            if a > answer:
                answer = a
    return answer