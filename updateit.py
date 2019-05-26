'''t=int(input())
for i in range(t):
    n,u=input().split(' ')
    n,u=[int(n),int(u)]
    l=[0]*n
    print(l)
    for j in range(u):
        d,r,val=input().split(' ')
        d,r,val=[int(d),int(r),int(val)]
        for x in range(d,r+1):
            l[x]=l[x]+val
    q=int(input())
    for h in range(q):
        m=int(input())
        print(l[m])'''

#NOP
t=input()
k=list(map(chr, range(65, 90)))
j=list(t)
l=[]
for i in range(len(j)):
    if j[i] in k:
        l.append(i)
i=0
c=0
if(len(l)>1):
    while(True):
        n=(l[i+1]-l[i])
        if(n<4):
            c=c+(4-(n))
        elif(n>4):
            while(n%4!=0):
                n+=1
                c+=1
        i+=1
        if (i==(len(l)-1)):
            print(c)
            break
else:
    print('0')
    



    
