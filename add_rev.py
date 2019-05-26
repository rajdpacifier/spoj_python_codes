p =int(input())
for i in range(p):
   Number1 , Number2 =raw_input().split(' ')
   Number1 , Number2 =[int(Number1) , int(Number2)]


   Reverse1= 0
   while(Number1 > 0):
       Reminder1 = Number1 %10
       Reverse1 = (Reverse1 *10) + Reminder1
       Number1 = Number1 //10


   Reverse2 = 0
   while(Number2 > 0):
       Reminder2 = Number2 %10
       Reverse2 = (Reverse2 *10) + Reminder2
       Number2 = Number2 //10
    
   add = Reverse1+Reverse2
   Reverse3 = 0
   while(add >0):
       reminder3 = add %10
       Reverse3 = (Reverse3 *10) +reminder3
       add =add //10

   print(int(Reverse3))    
                          