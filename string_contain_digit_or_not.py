s=input()
cnt=0
for i in range(len(s)):
    if s[i].isnumeric():
        cnt+=1
if cnt==0:
    print("Doesn't contain digit")
else:
    print("Contains",cnt,"digit")      