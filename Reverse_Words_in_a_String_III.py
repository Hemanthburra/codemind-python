s=input().split(" ")
r=[]
for i in range(len(s)):
    r.append(s[i][::-1])
print(" ".join(r))