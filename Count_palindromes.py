n=int(input())
v=list(map(int,input().split()))
f=[]
s=0
for i in range(len(v)):
    h=list(str(v[i]))
    f=v[i]
    #print(f,h[::-1])
    if list(str(f))==h[::-1]:
        s+=1
print(s)