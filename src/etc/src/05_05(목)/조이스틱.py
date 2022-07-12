# from string import ascii_uppercase

# def solution(name):
#     alph = {}
#     word = list("A"*len(name))
#     cnt = 0
#     answer = [0,0]
#     name_rever = name[0] + name[:0:-1]
#     name = list(name)
#     name_rever = list(name_rever)

#     for x in ascii_uppercase:
#         alph[x] = cnt
#         cnt += 1    
        
#     for i in range(len(name)):
#         if name == word:
#             break
#         s1 = alph[name[i]] - 0
#         s2 = 26 - alph[name[i]]
#         answer[0] += min(s1,s2) +1
#         word[i] = name[i]
    
#     word = list("A"*len(name))
#     for i in range(len(name_rever)):
#         if name_rever == word:
#             break
#         s1 = alph[name_rever[i]] - 0
#         s2 = 26 - alph[name_rever[i]]
#         answer[1] += min(s1,s2) +1
#         word[i] = name_rever[i]

#     return min(answer)-1

def solution(name):
    cnt = 0
    min_move = len(name)-1
    next_idx = 0
    
    while name[min_move] == 'A' and min_move > 0:
        min_move -= 1
    
    if min_move < 0:
        return cnt
        
    for idx, value in enumerate(name):
        cnt += min(ord(value)-ord('A'), ord('Z')-ord(value)+1)
        
        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
            
        min_move = min(min_move, idx + idx + len(name) - next_idx, idx + 2 * (len(name) - next_idx))
    
    cnt += min_move
    return cnt



name = "JEROEN"
name2 = "JAN"
name3 = "JABCADON"
name4 = "JBAAAAAV"
print(solution(name3))
# print(list(name.split('A')))
# print(list(name2.split('A')))
# print(list(name3.split('A')))
# print(list(name4.split('A')))