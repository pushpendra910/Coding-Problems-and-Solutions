def maxSubArraySum(arr,N):
        maxSum=float('-inf')
        curr_sum=0
        for element in arr:
            curr_sum+=element
            maxSum=max(maxSum,curr_sum)
            if curr_sum<0:
                curr_sum=0
        return maxSum

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    
    curr_sum=0
    mx=arr[0]
    flag=True
    for i in range(n):
        if curr_sum<0:
            curr_sum=0
            mx=arr[i]

        curr_sum+=arr[i]
        mx=max(mx,arr[i])
        if curr_sum>mx:
            print("NO")
            flag=False
            break
    
    if flag:
        print("YES")
