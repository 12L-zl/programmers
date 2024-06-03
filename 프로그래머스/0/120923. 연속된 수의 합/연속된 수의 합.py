def solution(num, total):
    answer = total // num # 몫
    
    result = []
    for i in range(answer - (num-1)//2, answer + (num+2)//2) :
        result.append(i)
    
    return result