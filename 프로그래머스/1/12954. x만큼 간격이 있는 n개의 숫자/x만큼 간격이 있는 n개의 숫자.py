def solution(x, n):
    answer = [x for _ in range(n)]
    
    for i in range(n-1) :
        answer[i+1] = answer[i] + x
        
    return answer