#!/usr/bin/env python
from math import *
import sympy as sp

class DoubleIntegral:

    def __init__(self, m, n, a, b, c, d, function, OfY=False, setting=0):
        self.m = m
        self.n = n
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.function = function
        self.OfY=OfY
        if ( OfY== True or setting == 0):
            self.deltaX = (b - a) / m
        if(OfY == False or setting == 0):
            self.deltaY = (d - c) / n
        if ( setting == 0 ):
            self.deltaA = self.deltaX * self.deltaY
        self.y = []
        self.arryLeft = []
        self.arryRight = []
        self.arryMid = []
        self.x = []
        self.arrxLeft = []
        self.arrxMid = []
        self.arrxRight = []

    def evaluateMidArea(self):
        areaLittle = self.deltaX*self.deltaY
        TotalArea = areaLittle*(self.m*self.n)
        print("Area MidPoint", TotalArea)

    def setx(self):
        for i in range(0, self.m + 1):
            if i == 0:
                self.x.append(self.a)
            else:
                self.x.append(self.x[i - 1] + self.deltaX)

        for i in range(0, self.m):
            if i == 0:
                self.arrxLeft.append(self.a)
            else:
                self.arrxLeft.append(self.arrxLeft[i - 1] + self.deltaX)

        for i in range(1, self.m + 1):
            if i == 1:
                self.arrxRight.append(self.a + self.deltaX)
            else:
                self.arrxRight.append(self.arrxRight[i - 2] + self.deltaX)

        for i in range(1, self.m + 1):
            middle = self.x[i - 1] + self.x[i]
            middle /= 2
            self.arrxMid.append(middle)
            
    def sety(self):
        for i in range(0, self.n + 1):
            if i == 0:
                self.y.append(self.c)
            else:
                self.y.append(self.y[i - 1] + self.deltaY)

        for i in range(0, self.n):
            if i == 0:
                self.arryLeft.append(self.c)
            else:
                self.arryLeft.append(self.arryLeft[i - 1] + self.deltaY)

        for i in range(1, self.n + 1):
            if i == 1:
                self.arryRight.append(self.c + self.deltaY)
            else:
                self.arryRight.append(self.arryRight[i - 2] + self.deltaY)

        for i in range(1, self.n + 1):
            middle = self.y[i - 1] + self.y[i]
            middle /= 2
            self.arryMid.append(middle)

    def evaluateMid(self):
        summ = 0
        for i in range(0, self.m):
            x = self.arrxMid[i]
            for j in range(0, self.n):
                y = self.arryMid[j]
                """print("Comparing", x, " and ", y)"""
                e = eval(self.function)
                summ += e * self.deltaA
        print("Mid Point: ", summ)

    def evaluateLLeft(self):
        summ=0
        for i in range(0,self.m):
            x=self.arrxLeft[i]
            for j in range(0,self.n):
                y=self.arryLeft[j]
                """print("Comparing",x," and ", y)"""
                e=eval(self.function)
                summ+=e*self.deltaA
        print("Lower Left Point: ", summ)

    def evaluateULeft(self):
        summ=0
        for i in range(0,self.m):
            x=self.arrxLeft[i]
            for j in range(0,self.n):
                y=self.arryRight[j]
                """print("Comparing",x," and ", y)"""
                e=eval(self.function)
                summ+=e*self.deltaA
        print("Upper Left Point: ", summ)

    def evaluateLRight(self):
        summ=0
        for i in range(0,self.m):
            x=self.arrxRight[i]
            for j in range(0,self.n):
                y=self.arryLeft[j]
                """print("Comparing",x," and ", y)"""
                e=eval(self.function)
                summ+=e*self.deltaA
        print("Lower Right Point: ", summ)

    def evaluateURight(self):
        summ=0
        for i in range(0,self.m):
            x=self.arrxRight[i]
            for j in range(0,self.n):
                y=self.arryRight[i]
                """print("Comparing",x," and ", y)"""
                e=eval(self.function)
                summ+=e*self.deltaA
        print("Upper Right Point: ", summ)
        
    def evaluateFunctionOfV(self):
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        if( self.OfY==True):
            self.function = sp.integrate(self.function,y)
            self.d="(("+self.d+")-y)"
            self.c="("+self.c+")"
            self.function = self.function.replace("y", self.d)
            self.function = self.function.replace("y", self.c)
            summ = 0
            for i in range( 0, self.m ):
                x = self.arrxMid[i]
                e=eval(str(self.function))
                summ+=e*self.deltaX
                
        else:
            self.function = sp.integrate(self.function,x)
            self.b = "(("+self.b+")-x)"
            self.a = "("+self.a+")"
            self.function = self.function.replace("x",self.b)
            self.function = self.function.replace("x",self.a)
            
            summ=0
            for i in range ( 0,self.n ):
                y = self.arryMid[i]
                e=eval(str(self.function))
                summ+=e*self.deltaY
        print(summ)
        

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")