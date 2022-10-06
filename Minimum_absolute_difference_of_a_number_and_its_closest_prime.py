import math
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

a=int(input())
l=[]
for i in range(a+a):
    if isprime(i):
        l.append(i)
        if i>a:
            break
if a in l:
    print(a-a)
elif abs(l[-1]-a)>=abs(l[-2]-a):
    print(abs(l[-2]-a))
elif abs(l[-1]-a)<abs(l[-2]-a):
    print(abs(l[-1]-a))
    
    

        