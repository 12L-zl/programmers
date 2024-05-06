from collections import defaultdict
# default값이 _자료형_ 인 dictionary

def solution(N, number):
    dp = defaultdict(set) # default가 set형인 딕셔너리
    
    for i in range(1, 9) :
        dp[i].add(int(str(N) * i)) # (set, {1 : {N}, 2 : {NN}, ..., 8 : {NNNNNNNN}})
        # dp[0] = set(), dp[1] = {N}
        
        for j in range(1, i) :
            for n1 in dp[j] :
                for n2 in dp[i - j] :
                    dp[i].add(n1 + n2)
                    dp[i].add(n1 - n2)
                    dp[i].add(n1 * n2)
                    if n2 != 0 :
                        dp[i].add(n1 // n2)
                        
        if number in dp[i] :
            return i
    return -1  # 최솟값이 8번보다 클 경우