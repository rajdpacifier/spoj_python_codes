p=int(raw_input())
for i in range (p):
    k=raw_input()
    t=len(l)
    for i in range(t):
        if l[i]==len(l)-1:
            l.remove(l[i])
            break
    j=max(l)
    print j