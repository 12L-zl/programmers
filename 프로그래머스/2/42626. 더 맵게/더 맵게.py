import heapq # append 와 sort 대신 사용하면 시간복잡도 감소

def solution(scoville, K):
    heap = []
    for i in scoville :
        heapq.heappush(heap, i)
    # heapq.heapify(scoville) # 최초 리스트에서 힙 정렬
    
    cnt = 0
    while heap[0] < K :
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        cnt += 1
        
        if len(heap) == 1 and heap[0] < K :
            return -1
    return cnt


'''
def solution(scoville, K):
    s = sorted(scoville)
    cnt = 0
    
    for i in s :
        if i < K :
            s.append(s[0] + s[1] * 2)
            s.sort()
            s = s[2:]  # 매번 정렬하면 시간복잡도 증가
            cnt += 1
        if s[0] > K :
            break
        if len(s) == 1 and s[0] < K :
            return -1
    return cnt
'''
    