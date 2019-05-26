
p =int(raw_input())
for i in range(p):
    a,b =raw_input().split(' ')
    a,b =[int(a),int(b)]
    if (a==0 and b==0):
        print ("0")
    elif (a==1 and b==1):
        print("1")
    elif(a==b and a%2==0):
        print(a*2)
    elif(a==b and a%2!=0):
        print (2*a-1)
    elif(a==b+2 and a%2==0):
        print (2*b+2)
    elif(a==b+2 and a%2!=0):
        print (2*b+1)    
    else:
        print("No Number")                    