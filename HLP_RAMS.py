for _ in xrange(int(raw_input())):
    n = int(raw_input())
    odds = 1 << bin(n).count('1') #It raises the no of 1's in N to the power of 2.
    print '{0} {1}'.format(n + 1 - odds, odds)