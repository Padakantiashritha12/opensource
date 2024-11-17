n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
for i in range(0,n-2):
    if a[i]<a[i+1]+a[i+2]:
        print(a[i]+a[i+1]+a[i+2])
        break
else:
    print(-1)
