def solution(s):
    num_ = {'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4',
           'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8',
           'nine' : '9', 'zero' : '0'}
    
    answer = s
    
    for key, value in num_.items() :
        answer = answer.replace(key, value)  # replace는 str -> str

    return int(answer)