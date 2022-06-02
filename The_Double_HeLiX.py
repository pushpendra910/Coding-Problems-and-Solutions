for _ in range(int(input())):
    s1=list(map(int,input().split()))
    s2=list(map(int,input().split()))
    intersections=[]
    i,j=1,1
    while(i<len(s1) and j<len(s2)):
        if s1[i]<s2[j]:
            i+=1
        elif s1[i]>s2[j]:
            j+=1
        else:
            intersections.append(s1[i])
            i+=1
            j+=1
    
    if len(intersections)==0:
        print(max(sum(s1),sum(s2)))
        continue

    sum1=[]
    sum2=[]
    k=0
    summ=0
    for i in range(1,s1[0]+1):
        if k>=len(intersections):
            summ+=s1[i]
            continue
        if s1[i]!=intersections[k]:
            summ+=s1[i]
        else:
            summ+=s1[i]
            sum1.append(summ)
            summ=0
            k+=1
    # print(summ)
    sum1.append(summ)
    k=0
    summ=0
    for i in range(1,s2[0]+1):
        if k>=len(intersections):
            summ+=s2[i]
            continue
        if s2[i]!=intersections[k]:
            summ+=s2[i]
        else:
            summ+=s2[i]
            sum2.append(summ)
            summ=0
            k+=1
    sum2.append(summ)
    s=0
    for i in range(len(sum1)):
        s+=max(sum1[i],sum2[i])

    print(s)
    # print(sum1)
    # print(sum2)
    # print(intersections)
