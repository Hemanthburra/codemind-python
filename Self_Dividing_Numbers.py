def isSelfDividing(n):
    
    a = set(list(str(n)))
    if('0' in a):
        return False
    for i in a:
        if(n%int(i)!=0):
            return False
    return True

left=int(input())
right=int(input())
result = []
for i in range(left, right+1):
    if(isSelfDividing(i)):
        result.append(i)
print(*result)
    