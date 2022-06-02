for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=1048575
    for i in range(n):
        if arr[i]!=i:
            ans&=arr[i]
        
    print(ans)
