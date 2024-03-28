def solution(n):
    
    '''
    # 방법 1)
    result = []
    
    for i in range(1, n) :
        if n % i == 1 :
            result.append(i)
            
    return min(result)



    '''
    # 방법 2) 약수 찾기
    result = []
    
    for i in range(2, n+1) :
        if (n-1) % i == 0 :
            result.append(i)
            
    return min(result)
    