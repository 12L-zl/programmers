def solution(s):
    s = s.lower()
    answer = True
    
    if s.count('p') == s.count('y') :
        answer = True
    else :
        answer = False
        
    return answer
