hour, min = map(int, input().split())

if min < 45:
    if hour == 0:
        hour = 24
    hour = hour - 1
    min = 60 - (45 - min)   
else:
    min = min - 45

print(hour, min)

