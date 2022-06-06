x=int(input())
s=list(map(int,input().split()))
d=len(s)//2
sum1=0
sum2=0
for i in range(len(s)):
    if i>=d:
        sum1+=s[i]
    else:
        sum2+=s[i]
print(sum2)
print(sum1)