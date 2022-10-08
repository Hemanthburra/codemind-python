s=input()
d=input()
cnt=0
for i in range(len(s)):
    if s[i] in d:
        cnt+=1
if cnt==0:
    print(-1)
else:
    print(cnt)