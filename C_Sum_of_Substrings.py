for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    sum=0
    for i in range(n-1):
        sum+=int(s[i])*10 + int(s[i+1])

    first=0
    last=0

    for i in range(n-1,-1,-1):
        if s[i]=='1':
            last=i
            break
    
    for i in range(n):
        if s[i]=='1':
            first=i
            break

    if s[first+1]=='1':
        sum-=2
    else:
        sum-=1

    
     



    print(sum)


    