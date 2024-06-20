def solution(s):
    s = sorted(s, reverse = True)
    # a > z / a -> z 내림차순
    # 대문자 < 소문자 / 소문자 -> 대문자 내림차순

    return ''.join(s)

# int - int.sort()
# str - sorted(str)