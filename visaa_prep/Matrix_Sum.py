n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
rs=[0]*n
cs=[0]*n
for i in range(n):
    for j in range(n):
        rs[i]+=a[i][j]
        cs[j]+=a[i][j]
k=[]
for i in range(n):
    k.append(rs[i]+cs[i])
print(" ".join(map(str,k)))
