import math
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
t=int(input())
for _ in range(t):
    a=int(input())
    l=[]
    for i in range(a+a):
        if isprime(i):
            l.append(i)
            if i>a:
                break
    if abs(l[-1]-a)>=abs(l[-2]-a):
        print(l[-2])
    elif abs(l[-1]-a)<abs(l[-2]-a):
        print(l[-1])
        
    

        