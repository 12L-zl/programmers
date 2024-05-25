def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)) :
        t = 100 - progresses[i]
        if t % speeds[i] == 0 :
            answer.append(t // speeds[i])
        else :
            answer.append((t // speeds[i]) + 1)   # [7, 3, 9]
            
    for i in range(len(answer) - 1) :
        if answer[i] > answer[i+1] :
            answer[i+1] = answer[i]  # [7, 7, 9]

    sets = set()
    result = []
    for i in answer :
        if i not in sets : # element 순서 유지
            result.append(answer.count(i))
            sets.add(i)
    return result