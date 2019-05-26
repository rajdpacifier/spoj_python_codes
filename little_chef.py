

from operator import add

p=input()
for i in range(p):
    sum0=0
    d=[]
    k=[]
    t=[]
    list_len=input()
    d = map(int,raw_input().split())

    print d
    for r in range(len(d)):
        sum0=sum0+d[r]
        k.append(sum0)
    
    for i in range (len(d)):
        sum1=0 
        for j in range(i,len(d)):
           
           sum1=sum1+d[j]
        t.append(sum1)
            
    f=map(add,k,t)
    print f    
    
    o=f.index(min(f))  
    print o+1 