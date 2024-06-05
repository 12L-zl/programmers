def solution(s):
    answer = []
    
    for i in s.split(' ') :
        answer.append(int(i)) # [1, 2, 3, 4]
    
    result = [min(answer), max(answer)]
    
    return str(result[0]) + ' ' + str(result[1])