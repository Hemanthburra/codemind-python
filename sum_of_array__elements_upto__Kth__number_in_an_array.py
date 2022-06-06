x=int(input()) 
s=list(map(int,input().split()))
f=int(input())
e=0
for i in range(len(s)):
    e+=s[i]
    if f==s[i]:
        break

print(e)