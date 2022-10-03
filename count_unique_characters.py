s=input()
s=list(s)
cnt=0
for i in range(len(s)):
    if s.count(s[i])==1 and s[i].islower():
        #print(s[i])
        cnt+=1
print(cnt)