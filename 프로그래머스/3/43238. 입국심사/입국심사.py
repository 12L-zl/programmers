def solution(n, times):
    answer = 0
    
    # right : 가장 비효율적 심사 시간
    left, right = 1, max(times) * n
    while left <= right :
        mid = (left + right) // 2
        people = 0  # 모든 심사관들이 mid분 동안 심사한 사람 수
        for time in times :
            people += mid // time
            # 모든 심사관 거치지 않아도 mid분 동안 n명 이상의 심사 할 수 있다면 종료
            if people >= n :
                break
        
        # 심사한 사람의 수 >= 심사 받아야할 사람의 수(n)
        if people >= n :
            answer = mid
            right = mid - 1
        else :
            left = mid + 1
    return answer