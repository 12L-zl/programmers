from collections import deque

def solution(n, edge):
    answer = 0
    # 연결된 노드 정보 그래프
    graph = [[] for _ in range(n+1)]
    # 각 노드 최단거리 리스트
    distance = [-1] * (n+1)
    
    for i in edge :
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    # [[],[3,2],[3,1,4,5],[6,4,2,1],[3,2],[2],[3]]
    
    q = deque([1]) # 출발 노드 = 1
    distance[1] = 0  # 출발 노드 최단거리 = 0
    
    while q :
        now = q.popleft() # 현재 노드
        
        for i in graph[now] : # 3, 2
            if distance[i] == -1 : # 방문하지 않은 노드
                q.append(i)
                distance[i] = distance[now] + 1
                # [-1, 0, 1, 1, 2, 2, 2]
                
    for j in distance :
        if j == max(distance) :
            answer += 1
    
    return answer