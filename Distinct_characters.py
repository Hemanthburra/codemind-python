s=input()
s=list(s)
cnt=0
d=[]
for i in range(len(s)):
    if s.count(s[i])==1 and s[i].islower():
        d.append(s[i])
        #print(s[i],end="")
d.sort()
print("".join(d))