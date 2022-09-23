n=int(input())
f=list(map(int,input().split()))
d=[]
j=len(f)-1
for i in range(len(f)//2):
    print(f[i],f[j],end=" ")
    j-=1
if len(f)%2==1:
    print(f[n//2],0,end=" ")