def solution(n):
    
    result = []
    
    for i in range(1, n) :
        if n % i == 1 :
            result.append(i)
            
    return min(result)



    '''
    result = []
    for i in range(1, n+1) :
        if (n-1) % i == 0 :
            result.append(i)
    return min(result)
    '''