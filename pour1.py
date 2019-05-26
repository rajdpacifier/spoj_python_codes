def gcd(a,b):
    while b > 0:
        temp=a%b
        a = b
        b = temp
    return a

def pour(A,B,C):
    a=A
    b=0
    c=1
    while a!=C and b!=C:
        x=min(B-b,a)
        a=a-x
        b=b+x
        c+=1
        if(a==C or b==C):
            break
        if(a==0):
            a=A
            c+=1
        if(b==B):
            b=0
            c+=1
    return c


t=int(raw_input())
while t>0:
    a=int(raw_input())
    b=int(raw_input())
    c=int(raw_input())
    if c>a and c>b:
        print "-1"
    elif a==c or b==c:
        print 1
    elif c%gcd(a,b)!=0:
        print -1
    else:
        x=min(pour(a,b,c),pour(b,a,c))
        print x
    t=t-1