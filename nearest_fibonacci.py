e=int(input())
#print(e)
d=[]
a=0
b=1
d.append(a)
d.append(b)
#print(a,b,end=" ")
while True:
    c=a+b
    #print(c,end=" ")
    d.append(c)
    a=b
    b=c
    if b>e:
        break
if abs(d[-1]-e)==abs(d[-2]-e):
    print(d[-2],d[-1])
elif abs(d[-2]-e)<abs(d[-1]-e):
    print(d[-2])
else:
    print(d[-1])
#print(d)