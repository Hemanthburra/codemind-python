t=['a','e','i','o','u','A','E','I','O','U']
r=input()
cnt=0
for i in range(len(r)):
    #print(r)
    if r[i] in t:
        cnt+=1
print(cnt)