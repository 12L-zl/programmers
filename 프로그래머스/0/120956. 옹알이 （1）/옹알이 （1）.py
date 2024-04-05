from itertools import permutations

def solution(babbling):
    noun = ['aya', 'ye', 'woo', 'ma']
    
    c = []
    for i in range(1, len(noun) + 1) : # 5
        com = permutations(noun, i)
        for j in com :
            c.append(j)

    
    lst = []
    for i in c :
        lst.append(''.join(i))
            
    
    cnt = 0
    for i in babbling:
        for j in lst :
            if i == j :
                cnt += 1
        
    return cnt
'''
if i in lst :
    cnt += 1
'''