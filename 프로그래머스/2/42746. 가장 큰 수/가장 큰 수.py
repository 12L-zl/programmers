def solution(numbers):
    answer = list(map(str, numbers))
    answer.sort(key = lambda x : x * 3, reverse = True)
    # 원소가 1000이하이기에 문자열 3자리수로 늘림
    # 3 -> 3 3 3
    # 30 -> 3 0 3 0 3 0
    # 34 -> 3 4 3 4 3 4
    # 34 > 3 > 30
    return str(int(''.join(answer)))

# str(''.join(answer)) - 11번 케이스 실패
# [0,0,0,0] 케이스인 경우, 문자열(answer) -> int -> str로 변경해주어야함