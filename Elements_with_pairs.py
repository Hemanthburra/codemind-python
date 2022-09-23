n=int(input())
f=list(map(int,input().split()))
if len(f)%2==0:
    print(*f)
else:
    f.append("0")
    print(*f)