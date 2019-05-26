for i in range(int(input())):
    l=list(map(int,input().split()))
    f=l[:2]
    sum=f[0]+f[1]
    for j in range((l[2])-2):
        f.append(f[j] + f[j+1])
        sum=sum+f[j+2]
    print(sum%l[3])  