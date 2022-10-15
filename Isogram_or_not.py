s=input()
s=list(s)
cnt=0
#print(s)
for i in range(len(s)):
    if s.count(s[i])==1:
        cnt+=1
#print(cnt,len(s))
if cnt==len(s):
    print(True)
else:
    print(False)