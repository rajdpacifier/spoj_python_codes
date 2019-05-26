
l=int(input())
while(l!=-1):
    if((l-1)%6==0):
        for i in range(0,int((l/6)+1)):
            if((3*i*(i+1)+1)==l):
                print("Y")
                break
            elif(i==l/6+1):
                print("N")
    else:
        print("N")
    l=int(input())

