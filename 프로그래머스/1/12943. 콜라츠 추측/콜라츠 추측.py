def solution(num):
    # 처음 num 이 1이면
    if num == 1 :
        return 0
    
    for i in range(500) :
        if num % 2 == 0 :
            num = num / 2
        else :
            num = num * 3 + 1
        
        if num == 1 :
            return i + 1
        
    return -1