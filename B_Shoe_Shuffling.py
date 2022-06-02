import contextlib


for _ in range(int(input())):
    n=int(input())
    shoes=list(map(int,input().split()))
    freq={}
    for s in shoes:
        if s in freq:
            freq[s]+=1
        else:
            freq[s]=1
        
    flag=False
    for element,count in freq.items():
        if count==1:
            print("-1")
            flag=True
            break
    if flag==True:
        continue
    
    students=[i for i in range(1,n+1)]
    for i in range(n-1):
        if shoes[i]==shoes[i+1]:
            temp=students[i]
            students[i]=students[i+1]
            students[i+1]=temp

    print(*students)
