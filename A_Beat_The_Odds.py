for _ in range(int(input())):
    n=int(input())
    numbers=list(map(int,input().split()))
    odd=0
    even=0
    for e in numbers:
        if e%2==0:
            even+=1
        else:
            odd+=1

    print(min(odd,even))
