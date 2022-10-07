n=int(input())
a=list(map(int,input().split()))
a=list(set(a))
#print(a)
a.sort()
#print(a)
if len(a)<3:
    print(max(a))
else:
    print(a[-3])