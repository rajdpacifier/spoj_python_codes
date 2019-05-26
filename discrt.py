def computeHCF(x, y):
    
   # This function implements the Euclidian algorithm to find H.C.F. of two numbers
   while(y):
       x, y = y, x % y

   return x
import math
n,k,a=map(int,input().split())
l=[]
for x in range(2,n):
    j=k*(math.log(x))
    h=math.log(a%n)
    if(j==k) and computeHCF(x,n)==1:
        l.append(x)
print(len(l))
for m in l:
    print(e)



