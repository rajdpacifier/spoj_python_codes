n,l,r=map(int,input().split())
k=list(map(int,input().split()))
count=0
for i in range(n):
    sum=k[i]
    for j in range(i+1,n):
        sum+=k[j]
        if sum>=l and sum<=r:
            count+=1
'''for e in k:
    if e>=l and e<=r:
        count+=1'''
print(count%1000000007)