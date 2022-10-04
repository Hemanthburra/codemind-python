n=int(input())
f=[]
for i in range(1,n*n):
    d=str(i)
    if str(i)==d[::-1]:
        f.append(int(d[::-1]))
        if int(str(i))>(n):
            break
n=int(n)
if n in f:
    f.remove(n)
if (abs((f[-1])-n))==(abs((f[-2]-n))):
    print(f[-2],f[-1])
elif (abs((f[-1]-n)))<(abs((f[-2]-n))):
    print(f[-1])
else:
    print(f[-2])