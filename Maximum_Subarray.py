def maximumSubarraySum(arr):
       n = len(arr)
       maxSum = -1e8
       currSum = 0

       for i in range(0, n):
           currSum = currSum + arr[i]
           if(currSum > maxSum):
               maxSum = currSum
           if(currSum < 0):
               currSum = 0
      
       return maxSum

n=int(input())
a=list(map(int,input().split()))

print(maximumSubarraySum(a))