
p = int(raw_input())
print " "
for i in range(p):
    raj=[]
    n=int(raw_input())
    for j in range(n):
        name = input()
        raj = raj + [name]
    n=0
    y    
    print " "    
    print raj    


    def perfect(n):
        fact=[]
    temp=0
    for i in range(1,0):
       if(n%i==0):
          fact.append(i)
    for i in range(len(fact)):
        temp=temp+fact[i]
    if(n==temp):
      return 'True'
    else:
       return 'False'
      
def depth(s):
    j=0
    f=[]
    temp=0
    for i in range(len(s)):
        if(s[i]=='('):
          j=j+1
        if(s[i]==')'):
          f.append(j)
          j=0
    for i in range(len(f)):
      if(f[i]>temp):
        temp=f[i]
    return temp

def sumsquares(l):
  temp=0
  for i in range(len(l)):
    if(l[i]**(0.5)-int(l[i]**(0.5))==0):
      temp=temp+l[i]
  return temp 