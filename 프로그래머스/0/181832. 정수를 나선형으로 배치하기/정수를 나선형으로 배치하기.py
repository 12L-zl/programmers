def solution(n):
    
    '''
    answer = [[0] * n for _ in range(n)]
    
    # 우, 하, 좌, 상
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    
    x, y = 0, 0
    answer[x][y] = 1
    k = 2
    
    while k <= n * n :
        for i in range(4) :
            
            while True :
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= n or nx < 0 or ny >= n or ny < 0 or answer[nx][ny] != 0:
                    break
                else :
                    answer[nx][ny] = k
                    x = nx
                    y = ny
                    k += 1
    
    return answer
    '''
    
    answer = [[0] * n for _ in range(n)]
    
    # 없으면 테스트 13 오류
    if n == 1 :
        return [[1]]
    
    x, y = 0, 0
    dir = 'r'
    
    for i in range(n*n) :
        answer[x][y] = i + 1
        
        if dir == 'r' : # 오른쪽
            y += 1  # (0, 0) -> (0, 1)
            if y == n-1  or  answer[x][y+1] != 0 :
                dir = 'd' # 아래쪽
        
        elif dir == 'd' :
            x += 1
            if x == n-1  or  answer[x+1][y] != 0 :
                dir = 'l' # 왼쪽
        
        elif dir == 'l' :
            y -= 1
            if answer[x][y-1] != 0 :
                dir = 'u' # 위쪽
        
        elif dir == 'u' :
            x -= 1
            if answer[x-1][y] != 0 :
                dir = 'r'
                
    return answer
    