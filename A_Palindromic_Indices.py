for _ in range(int(input())):
    n=int(input())
    s=input()
    mid=len(s)//2
    i,j=mid-1,mid+1
    count=1
    while(i>=0):
        if s[i]==s[mid]:
            count+=1
            i-=1
        else:
            break
    while(j<n):
        if s[j]==s[mid]:
            j+=1
            count+=1
        else:
            break
    print(count)