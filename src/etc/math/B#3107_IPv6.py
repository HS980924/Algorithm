# Upload BOJ Gold-5 math 3107번 IPv6
ipv6 = list(input().split(":"))
result = ""
max_length = 8

for i in range(len(ipv6)):
    num = ipv6[i]
    if len(num) == 0:
        if 0 < i and i < len(ipv6)-1:
            repeat = max_length-(len(ipv6)-1-i)
            for j in range(repeat):
                result += "0"*4 + ":"
        else:
            result += "0"*4 + ":"
    else:
        if len(num) < 4:
            result += "0"*(4-len(num))
        result += num + ":"
    max_length -= 1

print(result[:-1])

# 반례
# :0000::0001
# :0000:0011::0001:
# :0000:0001::0001
# ::1