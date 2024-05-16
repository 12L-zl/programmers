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
    # 다른 방법
    from collections import Counter
    
    answer = Counter(participant) - Counter(completion)
    # Counter 객체끼리 뺄 수 있음
    # {'vinko' : 1} - vinko가 1개 있음
    
    return list(answer.keys())[0]
    '''

    '''
    정확도 성공, 효율성 실패
    for i in completion :
        if i in participant :
            participant.remove(i)
            
    return participant[0]  # 단 한명의 선수만 완주 못했으니
                           # 한명이 아니라면 for문으로
    '''
    