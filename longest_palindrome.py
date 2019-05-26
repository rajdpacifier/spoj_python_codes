d=[]
b=[]
c=[]
count=0
N=int(input())
a=input()
for i in range((N-1),0,-1):
    for j in range(0,N-1):
        if a[j]==a[i]:
            b=a[j:i+1]
            
            c=b[::-1]
            if b==c:
                
                d.append(b)
k=list(set(d))
for i in k:
    if len(i)>count:
        count=len(i)
        word=i
print(len(word))    
print (word)         