l=[]
for i in range(int(input())):
    l.append(input())
c=1
p=l.count("1/4")
q=l.count("1/2")
r=l.count("3/4")
if(r!=0):
    z=min(p,r)
    c=c + z
    p=p-z
    r=r-z
c=c+(q//2)+r+(p//4)
q=q%2
p=p%4
if(q==1):
    if(p!=0):
        c+=1
        p-=1
    else:
        c+=1
if(p!=0):
    c+=1
print(c)



        

