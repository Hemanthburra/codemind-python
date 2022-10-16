s=input().lower()
f=input().lower()
for i in range(len(s)):
    if s.count(s[i])!=f.count(s[i]):
        print("False")
        break
else:
    print("True")