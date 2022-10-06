n=int(input())
arr=list(map(int,input().split()))
i=0
j=len(arr)-1
while i<=j:
    if arr[i]>=arr[j]:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
    else:
        j-=1
arr.sort()
print(*arr)