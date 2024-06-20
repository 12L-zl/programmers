def solution(s):
    answer = ''
    
    if len(s) % 2 != 0 :
        idx = int((len(s) + 1) / 2 - 1)
        return s[idx]
    else :
        idx1 = int(len(s) / 2 - 1)
        idx2 = int(len(s) / 2)
        return s[idx1] + s[idx2]        
