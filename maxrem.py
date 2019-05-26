k=int(input())
l=list(map(int,input().split()))
#l = [int(n) for n in input().split()]
l.sort()
l=list(set(l))
j=0
if(len(l)==1):
    print(j)
else:
    m=l[-2]%l[-1]
    print(m)