import math
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
t=int(input())
l=[]
cnt=0
for i in range(1,t+1):
    if t%i==0 :
        l.append(i)

for j in range(len(l)):
    if isprime(l[j]):
        continue
    else:
        cnt+=1
print(cnt)
    

        