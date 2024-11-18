a=int(input())
arr=list(map(int,input().split()))
b=int(input())
brr=list(map(int,input().split()))
m={}
n={}
for i in arr:
    m[i]=m.get(i,0)+1
for i in brr:
    n[i]=n.get(i,0)+1
k=[]
for i,f in n.items():
    if i not in m or m[i]<f:
        k.append(i)
print(*sorted(set(k)))
