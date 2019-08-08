n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
if(sum(a)==0):
    print("0")
else:
    print("".join(str(b) for b in a))
