def round(a):
    return int(a+0.5)
x0=int(input())
y0=int(input())
x1=int(input())
y1=int(input())
x,y=x0,y0
dx=x1 - x0
dy=y1 - y0

if (abs(dx) > abs(dy)):
    steps = abs(dx)
else:
    steps = abs(dy)
xinc = dx /float(steps)
yinc = dy /float(steps)
for v in range(steps):
    print(v)
    x+=xinc
    y+=yinc
    print(round(x),round(y))