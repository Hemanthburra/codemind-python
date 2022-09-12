s=input()
#s=s.split()
s=list(s)
cnt=0
for i in range(len(s)):
    if s[i]==" ":
        continue
    else:
        cnt+=1
print(cnt)