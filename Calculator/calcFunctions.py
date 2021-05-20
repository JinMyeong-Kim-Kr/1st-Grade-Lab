from math import factorial as fact
from keypad import *

romans = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
    (1, 'I')
]

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'

    if n>= 4000:
        return 'Error!'

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value
    
    return result



def romanToDec(numStr):
    try:
        n = 0
        for i in numStr:
            if i in numPadList or i in  operatorList:
                if i == 'C':
                    break
                return 'Error!'

        while numStr[0:] != '':
            for value, letters in romans:
                if numStr.find(letters) == 0:
                    n += value
                    numStr = numStr[len(letters):]
        return n

    except:
        return 'Error!'

