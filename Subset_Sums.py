from bisect import bisect_left
from bisect import bisect_right
n,a,b=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))

ss=[0]
for i in range(0,n):
    sum=arr[i]
    ss.append(sum)
    for j in range(0,n):
        sum+=arr[j]
        ss.append(sum)

ss.sort()
print(ss)
count=0
print(bisect_right(ss,b)-bisect_left(ss,a))
