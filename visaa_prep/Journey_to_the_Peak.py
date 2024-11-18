n=int(input())
a=list(map(int,input().split()))
s1=0
m=0
for i in a:
    s1+=i
    m=max(m,s1)
print(m)
