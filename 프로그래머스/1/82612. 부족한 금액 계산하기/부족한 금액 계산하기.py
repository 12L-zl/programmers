def solution(price, money, count):
    answer = []
    
    for i in range(1, count+1) :
        answer.append((price*i))
        
    if sum(answer) > money :
        result = sum(answer) - money
    else :
        result = 0
    

    return result