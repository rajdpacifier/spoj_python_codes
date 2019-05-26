p=int(raw_input())
for i in range(p):
    level=int(raw_input())
    block=1
    if level==1:
        print "1"
    else:
        
        for t in range(level+1):
            if t==1:
                result=1
                
            else:
                 result =block*5-(block-1)
                 block=block+t
                 t=t+1
                 
            
        print result 
