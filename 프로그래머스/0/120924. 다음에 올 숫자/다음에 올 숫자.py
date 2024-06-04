def solution(common):
    for i in range(len(common) - 2) :
        if common[i+1] - common[i] == common[i+2] - common[i+1] :
            answer = common[-1] + (common[i+1] - common[i])
        else :
            answer = common[-1] * (common[i+1] / common[i])
    
    return answer