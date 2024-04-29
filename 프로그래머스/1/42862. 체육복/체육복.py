def solution(n, lost, reserve):
    # reserve 중에서도 잃어버릴 수 있음
    # list 끼리 뺄 수 없으므로 set
    nlost = set(lost) - set(reserve)
    nreserve = set(reserve) - set(lost)
    
            
    for i in nreserve :
        if i - 1 in nlost :
            nlost.remove(i-1)
        elif i + 1 in nlost :
            nlost.remove(i+1)
            
    return n - len(nlost)