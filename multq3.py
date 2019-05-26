n,q=map(int,input().split())
l=[0]*(n+1)

for i in range(q):
    count=0
    sum=0
    a,b,c=map(int,input().split())
    if a==0:
        l[b:c]=map(lambda x : x+1, l[b:c])
        '''for j in range(b,c+1):
            l[j]=l[j]+1'''
    else:
        for k in range(b,c+1):
            k=str(l[k])
            for e in k:

                sum=sum+int(e)

            if (sum%3==0):
                count+=1
        print(count,l)