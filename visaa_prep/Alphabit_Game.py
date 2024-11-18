a=input()
v="aeiouAEIOU"
c="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
vc=0
cc=0
for i in a:
    if i in v:
        vc+=1
    elif i in c:
        cc+=1
print(f"{vc},{cc}")
