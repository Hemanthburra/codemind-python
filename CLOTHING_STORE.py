import collections
n=int(input())
l=list(map(int,input().split()))
#f=collections.Counter(l)
c=0
#print(f.items())
for i in set(l):
    c+=l.count(i)//2
    
print(c)