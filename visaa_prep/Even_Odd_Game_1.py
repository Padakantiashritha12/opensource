n=int(input())
s=0
r=0
while(n>0):
    r=n%10
    s+=r
    n=n//10
if(s%2==0):
    print("Vignesh")
else:
    print("Charan")
