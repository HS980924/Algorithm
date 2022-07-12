def transUpper(city):
    return [x.upper() for x in city]

def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if cacheSize <= 0:
        answer = len(cities)*5
    else:
        cities = transUpper(cities)
        next = 0
        
        for x in cities:
            if x not in cache:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(x)
                answer += 5
            else:
                answer += 1
                index = cache.index(x)            
                cache.append(cache.pop(index))
            
    return answer

size = 2
city = 	["Jeju", "Jeju", "Jeju", "Jeju", "Jeju"]
print(solution(size,city))