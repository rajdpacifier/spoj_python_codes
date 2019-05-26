
'''class InvalidFormat(Exception):
    pass

def getInput():
    rawInput = raw_input()

    # find the operator
    opIndex = -1
    for x in '+-*':
        opIndex = rawInput.find(x)
        if opIndex != -1: break
    if opIndex == -1: raise InvalidFormat

    operator = rawInput[opIndex]
    left = rawInput[0:opIndex]
    right = rawInput[opIndex + 1:]

    left = int(left)
    right = int(right)

    return left, right, operator

def doSimpleFormat(left, right, operator, result):
    leftStr = str(left)
    rightStr = operator + str(right)
    lineStr = '-'
    resultStr = str(result)

    # find the length of the longest line
    width = 0
    for x in [leftStr, rightStr, resultStr]:
        if len(x) > width: width = len(x)

    # right justify all of the lines
    tempStrList = []
    for x in [leftStr, rightStr, resultStr]:
        tempStrList.append(x.rjust(width))

    lineStr *= width
    leftStr, rightStr, resultStr = tempStrList

    return leftStr, rightStr, lineStr, resultStr
    

def doAddition(left, right):
    sumStr = str(left + right)
    return doSimpleFormat(left, right, '+', sumStr)

def doSubtraction(left, right):
    difStr = str(left - right)
    return doSimpleFormat(left, right, '-', difStr)

def doMultiplication(left, right):
    leftStr = str(left)
    rightStr = '*' + str(right)
    # firstLineStr is the line under left, right and operator
    firstLineStr = '-'
    # lineStr is the line under all of the operations
    lineStr = '-'
    resultStr = str(left * right)
    # each of the operations
    resultLines = []

    # here we make a line for each of the operations
    # reversed string of the right number
    workingRight = str(right)[::-1]
    i = 0
    for x in workingRight:
        thisResult = str(int(x) * left)
        rightSpacing = ' ' * i
        resultLines.append(thisResult + rightSpacing)
        i += 1
        
    # width of the first line
    width = 0
    for x in [leftStr, rightStr]:
        if width < len(x): width = len(x)
    firstLineStr = firstLineStr * width

    # find the length of the longest line
    width = 0
    for x in [leftStr, rightStr, resultStr] + resultLines:
        if width < len(x): width = len(x)

    lineStr = lineStr * width

    # combine the lines, right justified
    lines = []
    for x in [leftStr, rightStr, firstLineStr] + resultLines + [lineStr, resultStr]:
        lines.append(x.rjust(width))

    # if there's only one operation line, then we don't need the second line and result
    if len(str(right)) == 1:
        return lines[:-2]
    else:
        return lines

if __name__ == '__main__':
    t=int(input())
    while(t):
        try:
            left, right, operator = getInput()
        except InvalidFormat:
            pass
        except ValueError:
            pass
        else:
            if operator == '+':
                lines = doAddition(left, right)
            elif operator == '-':
                lines = doSubtraction(left, right)
            elif operator == '*':
                lines = doMultiplication(left, right)
            for x in lines:
                print x
        t-=1;'''
#!/usr/bin/env python
# -*- encoding: UTF-8 -*-
from sys import stdin

op = ['+', '-', '*']
inputs = stdin.readlines()
for _ in xrange(int(inputs[0])):
    expr = inputs[_ + 1].strip()
    i = 0
    t = expr.find(op[i])
    while t == -1:
        i += 1
        t = expr.find(op[i])

    expr = expr[:t], expr[t:]
    if i == 0:  # addition
        res = str(int(expr[0]) + int(expr[1][1:]))
        field = max(len(expr[0]), len(expr[1]), len(res))
        print '{0:>{1}}'.format(expr[0], field)
        print '{0:>{1}}'.format(expr[1], field)
        print '{0:>{1}}'.format('-'*max(len(res), len(expr[1])), field)
        print '{0:>{1}}'.format(res, field)
    
    elif i == 1:  # subtraction
        res = str(int(expr[0]) - int(expr[1][1:]))
        field = max(len(expr[0]), len(expr[1]), len(res))
        print '{0:>{1}}'.format(expr[0], field)
        print '{0:>{1}}'.format(expr[1], field)
        print '{0:>{1}}'.format('-'*max(len(expr[1]), len(res)), field)
        print '{0:>{1}}'.format(res, field)
    
    else:  # multiplication
        a = int(expr[0])
        tmp = expr[1][1:]
        b = int(tmp)
        res = []
        for x in reversed(tmp):
            res.append(str(a*int(x)))
        finres = str(a * b)
        field = max(len(expr[0]), len(expr[1]), len(finres), len(res[-1]) + len(res) - 1)
        print '{0:>{1}}'.format(expr[0], field)
        print '{0:>{1}}'.format(expr[1], field)
        print '{0:>{1}}'.format('-'*max(len(res[0]), len(expr[1])), field)
        if len(res) != 1:
            for x in xrange(len(res)):
                print '{0:>{1}}{2:<{3}}'.format(res[x], field - x, ' ', x)
            print '{0:>{1}}'.format('-'*(max(len(res[-1]) + len(res) - 1, len(finres))), field)
        print '{0:>{1}}'.format(finres, field)       