def factor(a):
    n=0
    for i in range(1,a+1):
        if a%i==0:
            n+=1
    if n==2:
        return True
    else:
        return False
v=int(input())
h=list(map(int,input().split()))
y=0
for i in range(len(h)):
    if factor(h[i]):
        y+=1
print(y)
        
