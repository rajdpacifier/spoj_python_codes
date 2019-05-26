t=int(input())
for i in range(t):
    n,m=map(int,input().split(' '))
    l=list(map(int,input().split(' ')))
    l.sort()
    sum=0
    for j in range(m):
        sum=sum +l[j]
    if(sum>0):
        break
    else:
        print(-sum)



