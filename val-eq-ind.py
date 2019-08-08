b=[]
n=int(input())
a=list(map(int,input().split()))[:n]
for i in range(n):
  if a[i] is i:
    b.append(i)
if b==[]:
  print("-1")
else:
  b.sort()
  print(*b)
