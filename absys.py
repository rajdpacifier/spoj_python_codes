for i in range(int(input())):
    input()
    k = input().split()
    for item in k:
        if "machula" in item:
            l= k.index(item)
    if l== 0:
        k[2], k[4] = int(k[2]), int(k[4])
        print("{} + {} = {}".format(k[4] - k [2], k[2], k[4]))
    elif l== 2:
        k[0], k[4] = int(k[0]), int(k[4])
        print("{} + {} = {}".format(k[0], k[4] - k[0], k[4]))
    else:
        k[0], k[2] = int(k[0]), int(k[2])
        print("{} + {} = {}".format(k[0], k[2], k[0] + k[2]))