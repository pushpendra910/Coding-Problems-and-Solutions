import math as m

def number(times,p,mid):
    count=0
    for t in times:
        count=count+(m.sqrt(((8*mid)/t) +1) -1 )/(2*t)
    
    if count>=p:
        return True
    else:
        return False
        
if __name__=='__main__':
    for _ in range(int(input())):
        p=int(input())
        arr=list(map(int,input().split()))
        times=[arr[i] for i in range(1,len(arr))]
        times.sort()
        low=0
        high=p*times[-1]
        ans=0
        while(low<=high):
            mid=(low+high)//2
            if number(times,p,mid):
                ans=mid 
                high=mid-1
            else:
                low=mid+1

        print(ans)