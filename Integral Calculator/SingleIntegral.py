#!/usr/bin/env python
from math import *

def evaluate(arr,n, deltaX,function):  
    summ = 0 
    for i in range ( 0, n ):
        x=arr[i]
        e=eval(function)
        summ += e*deltaX
    return summ
    
def LineLength(a,b):
    print("Length of line ", b-a)
    
def SIOption(n,a,b,function):
    summ=0
    n=int(n)
    a=float(a)
    b=float(b)
    
    if ( function == "1"):
        LineLength(a,b)
        
    else:
        deltaX = (b-a)/n
        x=[]
        arrxLeft =[]
        arrxRight = []
        arrxMid = []
    
        for i in range(0, n + 1):
            if i == 0:
                x.append(a)
            else:
                x.append(x[i - 1] + deltaX)

        for i in range(0, n):
            if i == 0:
                arrxLeft.append(a)
            else:
                arrxLeft.append(arrxLeft[i - 1] + deltaX)

        for i in range(1, n + 1):
            if i == 1:
                arrxRight.append(a + deltaX)
            else:
                arrxRight.append(arrxRight[i - 2] + deltaX)

        for i in range(1, n + 1):
            middle = x[i - 1] + x[i]
            middle /= 2
            arrxMid.append(middle)   
    
        summ = evaluate(arrxMid,n,deltaX,function)
        print("MidPoint: ", summ)
        summ = evaluate(arrxLeft,n,deltaX,function)
        print("LeftPoint: ", summ)
        summ = evaluate(arrxRight,n,deltaX,function)
        print("Rightpoint: ", summ)
    
