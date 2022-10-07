x,y=map(int,input().split())
#print(x,y)
if x%2:
    print("NO")
elif (x==0 and y%2):
    print("NO")
else:
    print("YES")