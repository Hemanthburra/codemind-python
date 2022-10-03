n=int(input())
d=n*n
i=n*n
s=0
while d>0:
    f=d%10
    s+=f
    d=d//10
#print(i,s)
if n==s:
    print("Neon Number")
else:
    print("Not Neon Number")