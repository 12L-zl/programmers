def solution(lines):
    
    sets = [set(range(min(l), max(l))) for l in lines]
    # [{0}, {2, 3, 4}, {3, 4, 5, 6, 7, 8}]
    
    answer = sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2]
    # set에서 & : 교집합 / | : 합집합
    # {3, 4}
    
    return len(answer)