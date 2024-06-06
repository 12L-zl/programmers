def solution(x):
    answer = True
    
    a = []
    for i in str(x) :
        a.append(int(i))
    s = sum(a)

    if x % s == 0 :
        answer = True
    else :
        answer = False
    
    return answer