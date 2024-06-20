import math

def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        if int(math.sqrt(i)) ** 2 == i: # 제곱근 있는 숫자는 약수의 개수가 홀수
            answer -= i
        else:
            answer += i

    return answer