'''mo=['January','February','March','April','May','June','July','August','September','October','November','December']
for i in range(int(raw_input())):
    n=int(raw_input())
    l=bin(n)
    d=int(l[(len(l))-5:len(l)],2)
    m=int(l[(len(l))-9:(len(l))-5],2)
    y=int(l[2:(len(l))-9],2)
    print d,mo[m-1],y'''

#ALCATRAZ1

'''t=int(input())
for i in range(t):
    k=input()
    k=list(k)
    print(k)
    sum=0
    for j in range(len(k)):
	    sum+=int(k[j])
    print(sum)'''

t=int(input())
k=[]
c=0

for i in range(t):
    for j in range(t):
        c+=1
        k.append(str(c))
    p=" ".join(k)
    print(p)
    k=[]
    


        
