p =int(raw_input())
for i in range(p):
    k=int(raw_input())
    g=0
    
    a=[]
    a = [int(x) for x in raw_input().split()]    
    for l in range(0,len(a)-1):
        for m in range(l+1,len(a)-1):
            t=(a[l]+a[m])/2
            for i in range(len(a)-1):
                if(a[i]==t):
                    g=g+1
    print(g)