from collections import defaultdict
def solution(genres, plays):
    answer = []
    dictSum = defaultdict(int)
    dictGenres = defaultdict(list)
    
    for idx in range(len(genres)):
        dictSum[genres[idx]] += plays[idx]
        dictGenres[genres[idx]].append((idx,plays[idx]))
    
    for key in sorted(dictSum,key=lambda x:dictSum[x],reverse=True):
        dictGenres[key].sort(key=lambda x:(x[1],-x[0]))
        cnt = 0
        while dictGenres[key] and cnt < 2:
            value = dictGenres[key].pop()
            answer.append(value[0])
            cnt += 1
    
    return answer
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))