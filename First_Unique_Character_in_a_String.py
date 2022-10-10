s=input()
cnt=0
for i in range(len(s)):
    if s.count(s[i])==1:
        print(i)
        cnt=1
        break
if cnt==0:
    print(-1)