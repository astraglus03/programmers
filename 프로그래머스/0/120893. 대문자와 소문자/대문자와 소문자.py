def solution(my_string):
    # swapcase()사용시 대소문자 변경해줌
    answer = ''
    for i in range(0,len(my_string)):
        if(my_string[i].islower()):
            answer+=my_string[i].upper()
        else:
            answer+=my_string[i].lower()
    return answer