a=int(input())
a1=a**2
f=0
#print(a)
while a>0:
    d=a%10
    f=f*10+d
    a=a//10
f1=f**2
a1=list(str(a1))
f1=list(str(f1))
if a1[::-1] == f1:
    print(True)
else:
    print(False)
    
    