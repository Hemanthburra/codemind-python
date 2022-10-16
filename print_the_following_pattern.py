t=int(input())
k=list('x')*t
k[0]='0'
for i in range(t):
    print("".join(k))
    if i==len(k):
        break
    k[i],k[i+1]=k[i+1],k[i]