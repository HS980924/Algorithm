def solution(files):
    answer = []
    arr = []
    
    for file in files:
        head = ''
        number = ''
        tail = ''
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                
                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
                arr.append([head,number,tail])
                break
        
    sort_arr = sorted(arr, key=lambda x : (x[0].lower(), int(x[1])))

    for x in sort_arr:
        tmp = "".join(x)
        answer.append(tmp)
    
    return answer


files =  ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
#files = ["F-5 ", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(files))