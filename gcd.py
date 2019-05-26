
def find_gcd(x, y): 
      
    while(y): 
        x, y = y, x % y 
      
    return x 

t=[]
k=int(input())
for i in range(k):
    
    f=1
    l=list(map(int,input().split(' ')))
    for j in range(1,len(l)):
        f=f*l[j]
    t.append(f)          
num1 = t[0] 
num2 = t[1] 
gcd = find_gcd(num1, num2) 
  
for i in range(2, len(t)): 
    gcd = find_gcd(gcd, t[i]) 
      
print(gcd) 
  