n=int(input())
#print(n)
c=[]
a=0
b=1
c.append(a)
c.append(b)
for i in range(n):
    d=a+b
    c.append(d)
    a=b
    b=d
    if n==d:
        break
if n in c:
    print(True)
else:
    print(False)