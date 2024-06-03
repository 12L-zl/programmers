import math

def solution(numer1, denom1, numer2, denom2):
    answer = [numer1 * denom2 + denom1 * numer2, denom1 * denom2]
    
    # 최대공약수 계산
    gcd = math.gcd(answer[1], answer[0])
    
    result = [answer[0] / gcd, answer[1] / gcd]
    
    return result