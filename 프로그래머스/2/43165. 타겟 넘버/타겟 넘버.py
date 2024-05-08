from collections import defaultdict
from itertools import product

def solution(numbers, target):
    lst = defaultdict(list)     # numbers의 양수 음수 (더하기,빼기만 되므로)
    answer = defaultdict(list)  # numbers 부호 가능한 조합
    
    comb = list(product([0, 1], repeat = len(numbers)))  # 0(+)과 1(-)로 이루어진 len(numbers)자리 조합
    com = []
    for i in comb :
        com.append(i)

    for i in range(len(numbers)) :
        lst[i].extend([numbers[i], -numbers[i]])
        for j in range(len(com)) : 
            k = com[j][i]
            answer[j].append(lst[i][k])
    
    # 키 값별 value 합
    result = dict()
    for key, value in answer.items() :
        values = sum(value)
        result[key] = values
    
    # target과 같은 값 개수 세기
    cnt = 0
    for key, value in result.items() :
        if target == value :
            cnt += 1
        
    return cnt