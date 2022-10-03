s=int(input())
l=int(input())
for i in range(s,l+1):
    s1=list(str(i))
    v=list(str(i))
    if s1==v[::-1]:
        print("".join(s1),end=" ")
        