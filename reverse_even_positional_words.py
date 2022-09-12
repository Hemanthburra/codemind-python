s=input()
r=s.split()
for i in range(len(r)):
    if i%2==0:
        t=r[i]
        print(t[::-1],end=" ")
    else:
        print(r[i],end=" ")