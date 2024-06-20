def solution(seoul):
    for index, str_ in enumerate(seoul) :
        if 'Kim' in str_ :
            answer = '김서방은 ' + str(index) + '에 있다'
    return answer