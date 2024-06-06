def solution(n):
    answer = []
    for i in str(n) :
        answer.append(int(i)) # [1, 1, 8, 3, 7, 2]
        
    answer.sort(reverse = True)
    
    result = ''
    for i in answer :
        result += str(i)
        
    return int(result)