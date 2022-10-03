s=input()
s=list(s)
s=set(s)
s=list(s)
s.sort()
s=list(s)
for i in range(len(s)):
    if s[i].isupper() or s[i]==" ":
        continue
    else:
        print(s[i],end="")
    
    
    