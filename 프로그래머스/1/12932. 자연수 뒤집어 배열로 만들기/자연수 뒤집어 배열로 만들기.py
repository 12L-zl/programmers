def solution(n):
    answer = []
    
    for i in str(n) :
        answer.append(int(i))
    
    answer.reverse() # list(reversed(answer))
    
    return answer
