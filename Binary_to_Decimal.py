t=int(input())
for _ in range(t):
    r=int(input())
    r=list(str(r))
    r.reverse()
    s=0
    for i in range(len(r)):
        s+=int(r[i])*(2**i)
    print(s)
        