for i in range(int(input())):
    
    s,f=map(int,input().split())
    k=list(map(int,input().split()))
    j=0
    k.sort()
    k=k[::-1]
    count=0
    print("Scenario #"+str(i+1)+":")
    while(s>0 and f>0):
        s-=k[j]
        #print(s)
        j+=1
        count+=1
        f-=1
    if(s>0):
        print("impossible")
    else:
        print(count)
    print("\n")
