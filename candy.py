t=int(input())
for i in range(t):
    o=input()
    n=int(input())
    l=[]
    sum=0
    for j in range(n):
        k=int(input())
        l.append(k)
    for e in l:
        sum=sum+e
    if(sum%n==0):
        print("YES")    
    else:
        print("NO")
