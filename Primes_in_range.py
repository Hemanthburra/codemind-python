import math
def sq(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True

a=int(input())
b=int(input())
cnt=0
for i in range(a,b+1):
    if sq(i):
        cnt+=1
print(cnt)