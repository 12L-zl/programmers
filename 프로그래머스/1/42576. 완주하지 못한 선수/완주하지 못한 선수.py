def solution(participant, completion):
    # 정렬하여 비교하기 쉽게
    # 같은 인덱스의 이름이 같으면 완주 함
    # 같은 인덱스의 이름이 다르면 완주 못함
    participant.sort()
    completion.sort()
    
    for a, b in zip(participant, completion) :
        if a != b :
            return a
    
    return participant[-1] # 마지막 참가자
    
    
    '''
    정확도 성공, 효율성 실패
    for i in completion :
        if i in participant :
            participant.remove(i)
            
    return participant[0]  # 단 한명의 선수만 완주 못했으니
                           # 한명이 아니라면 for문으로
    '''
