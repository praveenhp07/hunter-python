def Dup(x): 
    size = len(x) 
    dup = [] 
    for i in range(size): 
        k = i + 1
        for j in range(k, size): 
            if x[i] == x[j] and x[i] not in dup: 
                dup.append(x[i])
    return dup 
n=int(input())
a=list(map(int,input().split()))[:n]
a.sort()
if Dup(a)==[]:
    print("unique")
else:
    print(*Dup(a))
