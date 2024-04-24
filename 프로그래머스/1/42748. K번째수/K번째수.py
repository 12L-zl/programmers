def solution(array, commands):
    answer = []
    
    for com in commands :
        i, j, k = com  
        nary = array[i-1 : j]
        nary.sort()
        answer.append(nary[k-1])
    
    return answer