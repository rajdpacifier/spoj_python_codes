for i in range(int(input())):
    empty = raw_input()
    x = int(input())
    y = 0
    for j in range(x):
        y = (y+input()%x)%x
    if y%x==0:
        print ("YES")
    else:
        print ("NO")