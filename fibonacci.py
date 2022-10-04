n=int(input())
#print(n)
c=[]
a=0
b=1
c.append(a)
c.append(b)
for i in range(n-2):
    d=a+b
    c.append(d)
    a=b
    b=d
print(*c)