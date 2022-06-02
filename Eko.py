
def ispossible(mid,heights,m):
    h=0
    for x in range(len(heights)):
        if heights[x]>=mid:
            h=h+heights[x]-mid
        else:
            break
    
    if h>=m:
        return True
    else:
        return False

if __name__=="__main__":
    n,m=map(int,input().split())
    heights=list(map(int,input().split()))
    heights.sort(reverse=True)

    low=0
    high=max(heights)
    ans=high
    while(low<=high):
        mid=(high+low)//2
        if ispossible(mid,heights,m):
            low=mid+1
            ans=mid
        else:
            high=mid-1
        
    print(ans)