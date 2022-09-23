u=int(input())
h=list(map(int,input().split()))
g=0
p=0
for i in range(len(h)):
    if h[i]%2==1 and i%2==1:
        g+=1
    if h[i]%2==1:
        p+=1
if g==p:
    print("True")
else:
    print("False")