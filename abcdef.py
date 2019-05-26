#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from sys import stdin


def main():
    stdin.readline()
    s = map(int, stdin)
    efd = []
    abc = []
    count = 0
    print(s)
    for e in s:
        for f in s:
            for d in s:
                efd.append((e + f) * d)
                abc.append(e * f + d)
    efdh = {}
    for x in efd:
        try:
            efdh[x] += 1
        except KeyError:
            efdh[x] = 1
    for x in abc:
        try:
            count += efdh[x]
        except KeyError:
            pass
    print (count)

main()


