n = int(raw_input())
a = b = int(raw_input())
for x in xrange(n - 1):
    tmp = int(raw_input())
    a |= tmp
    b &= tmp
print a & (~b)