
if __name__=='__main__':
    for _ in range(int(input())):
        n=int(input())
        arr=list(map(int,input().split()))
        freq={}
        for i in range(n):
            if arr[i] in freq:
                freq[arr[i]]+=1
            else:
                freq[arr[i]]=1

        t,s=0,0

        for key,value in freq.items():
            if value>=2:
                t+=1
            else:
                s+=1

        print(t+(s+1)//2)
    
