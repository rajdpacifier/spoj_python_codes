



while True:
     a , b, c = raw_input().split(' ')
     a , b, c = [int(a) ,int(b) ,int(c)]
     if (a==0 and b==0 and c==0):
         break
     elif(b-a==c-b and b-a!=0):
         d=c+(b-a)
         print("AP " + str(d))
     elif (b/a==c/b and b/a!=1):
         e=c*b/a
         print("GP " + str(e))
     