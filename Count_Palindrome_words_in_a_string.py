def palin(s):
    if s==s[::-1]:
        return True
    return False



s=input().lower().split()
#s.split(" ")
cnt=0
for i in range(len(s)):
    if palin(s[i]):
        cnt+=1
print(cnt)