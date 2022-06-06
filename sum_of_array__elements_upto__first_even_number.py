x=int(input()) 
s=list(map(int,input().split()))
f=0
for i in range(len(s)):
    
    if s[i]%2==0:
        break
    f+=s[i]
print(f)