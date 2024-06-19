import heapq

def solution(jobs):
    answer = 0
    now, i, start = 0, 0, -1  # 현재 시간, 처리 개수, 마지막 완료시간
    heap = []
    
    while i < len(jobs) :
        for job in jobs :
            if start < job[0] <= now :  
                heapq.heappush(heap, [job[1], job[0]])  # 작업시간 작은 것부터 나열 [3,0], [6,2], [9,1]
        
        if heap :
            current = heapq.heappop(heap) 
            start = now
            now += current[0] 
            answer += (now - current[1]) 
            i += 1
        else :
            now += 1
            
    answer = answer // len(jobs)
    
    return answer