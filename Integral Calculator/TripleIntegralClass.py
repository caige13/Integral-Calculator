#!/usr/bin/env python
from math import *
import sympy as sp

class TripleIntegral:
    
    def __init__(self,m,n,p,a,b,c,d,e,f,function,deltaX,deltaY,deltaZ):
        self.m = m
        self.n=n
        self.p=p
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
        self.function=function
        self.y = []
        self.arryMid = []
        self.x = []
        self.arrxMid = []
        self.z = []
        self.arrzMid = []
        self.deltaX = deltaX
        self.deltaY = deltaY
        self.deltaZ = deltaZ
        
    def setx(self):
        for i in range(0, self.m + 1):
            if i == 0:
                self.x.append(self.a)
            else:
                self.x.append(self.x[i - 1] + self.deltaX)
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
        for i in range(1, self.n + 1):
            middle = self.y[i - 1] + self.y[i]
            middle /= 2
            self.arryMid.append(middle)
            
    def setz(self):
        for i in range(0, self.p + 1):
            if i == 0:
                self.z.append(self.e)
            else:
                self.z.append(self.z[i - 1] + self.deltaZ)
        for i in range(1, self.p + 1):
            middle = self.z[i - 1] + self.z[i]
            middle /= 2
            self.arrzMid.append(middle)
    
    def setFunction(self, function):
        self.function = function
        
    def getdy(self):
        y = sp.Symbol('y')
        self.function = sp.integrate(self.function,y)
        self.d = "(("+self.d+")-y)"
        self.c = "("+self.c+")"
        self.function = self.function.replace("y",self.d)
        self.function = self.function.replace("y",self.c)
        return self.function
    
    def getdx(self):
        x = sp.Symbol('x')
        self.function = sp.integrate(self.function, x)
        self.b = "(("+self.b+")-x)"
        self.a = "("+self.a+")"
        self.function = self.function.replace("x", self.b)
        self.function = self.function.replace("x", self.a)
        return self.function
    
    def getdz(self):
        z = sp.Symbol('z')
        self.function = sp.integrate(self.function,z)
        self.f = "(("+self.f+")-y)"
        self.e = "("+self.e+")"
        self.function = self.function.replace("z",self.f)
        self.function = self.function.replace("z",self.e)
        return self.function
    
    def getSingleNumericalx(self):
        summ = 0
        x = sp.Symbol('x')
        for i in range( 0, self.m ):
                x = self.arrxMid[i]
                e=eval(str(self.function))
                summ+=e*self.deltaX
        print(summ)
    
    def getSingleNumericaly(self):
        summ=0
        y = sp.Symbol('y')
        for i in range( 0, self.n ):
                y = self.arryMid[i]
                e=eval(str(self.function))
                summ+=e*self.deltaY
        print(summ)
    
    def getSingleNumericalz(self):
        z = sp.Symbol('z')
        summ=0
        for i in range( 0, self.p ):
                z = self.arrzMid[i]
                e=eval(str(self.function))
                summ+=e*self.deltaZ
        print(summ)
        
    def getDoubleNumericalxy(self):
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        deltaA = deltaX*deltaY
        summ = 0
        for i in range(0, self.m):
            x = self.arrxMid[i]
            for j in range(0, self.n):
                y = self.arryMid[j]
                """print("Comparing", x, " and ", y)"""
                e = eval(self.function)
                summ += e * deltaA
        print(summ)
        
    def getDoubleNumericalxz(self):
        x = sp.Symbol('x')
        z = sp.Symbol('z')
        deltaA = deltaX*deltaZ
        summ = 0
        for i in range(0, self.m):
            x = self.arrxMid[i]
            for j in range(0, self.p):
                z = self.arrzMid[j]
                """print("Comparing", x, " and ", z)"""
                e = eval(self.function)
                summ += e * deltaA
        print(summ)
        
    def getDoubleNumericalyz(self):
        y = sp.Symbol('y')
        z = sp.Symbol('z')
        deltaA = deltaY*deltaZ
        summ = 0
        for i in range(0, self.n):
            y = self.arryMid[i]
            for j in range(0, self.p):
                z = self.arrzMid[j]
                """print("Comparing", x, " and ", z)"""
                e = eval(self.function)
                summ += e * deltaA
        print(summ)
    
    def getTripleNumerical(self):
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        z = sp.Symbol('z')
        summ = 0
        deltaV = self.deltaX*self.deltaY*self.deltaZ
        for i in range (0,self.m):
            x = self.arrxMid[i]
            for j in range(0,self.n):
                y = self.arryMid[j]
                for u in range (0,self.p):
                    z=self.arryzMid[u]
                    e=eval(self.function)
                    summ+=e*self.deltaV
    
    """def Orderdxdydz2Function(self):
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        z = sp.Symbol('z')
        summ = 0
        self.function = sp.integrate(self.function, x)
        self.b = "(("+self.b+")-x)"
        self.a = "("+self.a+")"
        self.function = self.function.replace("x", self.b)
        self.function = self.function.replace("x", self.a)
        self.function = sp.integrate(self.function,y)
        self.d = "(("+self.d+")-y)"
        self.c = "("+self.c+")"
        self.function = self.function.replace("y",self.d)
        self.function = self.function.replace("y",self.c)
        for i in range( 0, self.p ):
                z = self.arrzMid[i]
                e=eval(str(self.function))
                summ+=e*self.deltaZ
        print(summ)
    
    def Orderdydxdz2Function(self):
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        z = sp.Symbol('z')
        summ = 0
        self.function = sp.integrate(self.function,y)
        self.d = "(("+self.d+")-x)"
        self.c = "("+self.c+")"
        self.function = self.function.replace("y", self.d)
        self.function = self.function.replace("y", self.c)
        self.function = sp.integrate(self.function,x)
        self.b = "(("+self.b+")-y)"
        self.a = "("+self.a+")"
        self.function = self.function.replace("x",self.b)
        self.function = self.function.replace("x",self.a)
        for i in range( 0, self.p ):
                z = self.arrzMid[i]
                e=eval(str(self.function))
                summ+=e*self.deltaZ
        print(summ)
        
    def Orderdxdzdy2Function(self):
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        z = sp.Symbol('z')
        summ = 0
        self.function = sp.integrate(self.function,x)
        self.b = "(("+self.b+")-x)"
        self.a = "("+self.a+")"
        self.function = self.function.replace("x", self.b)
        self.function = self.function.replace("x", self.a)
        self.function = sp.integrate(self.function,z)
        self.f = "(("+self.f+")-y)"
        self.e = "("+self.e+")"
        self.function = self.function.replace("z",self.f)
        self.function = self.function.replace("z",self.e)
        for i in range( 0, self.n ):
                z = self.arryMid[i]
                e=eval(str(self.function))
                summ+=e*self.deltaY
        print(summ)
        
    def Orderdzdxdy2Function(self):
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        z = sp.Symbol('z')
        summ = 0
        self.function = sp.integrate(self.function,z)
        self.f = "(("+self.f+")-x)"
        self.e = "("+self.e+")"
        self.function = self.function.replace("x", self.f)
        self.function = self.function.replace("x", self.e)
        self.function = sp.integrate(self.function,x)
        self.b = "(("+self.b+")-y)"
        self.a = "("+self.a+")"
        self.function = self.function.replace("z",self.b)
        self.function = self.function.replace("z",self.a)
        for i in range( 0, self.n ):
                z = self.arryMid[i]
                e=eval(str(self.function))
                summ+=e*self.deltaY
        print(summ)
    
    def Orderdzdydx2Function(self):
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        z = sp.Symbol('z')
        summ = 0
        self.function = sp.integrate(self.function,z)
        self.f = "(("+self.f+")-x)"
        self.e = "("+self.e+")"
        self.function = self.function.replace("x", self.f)
        self.function = self.function.replace("x", self.e)
        self.function = sp.integrate(self.function,x)
        self.d = "(("+self.d+")-y)"
        self.c = "("+self.c+")"
        self.function = self.function.replace("z",self.d)
        self.function = self.function.replace("z",self.c)
        for i in range( 0, self.m ):
                z = self.arrxMid[i]
                e=eval(str(self.function))
                summ+=e*self.deltaX
        print(summ)
        
    def Orderdydzdx2Function(self):
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        z = sp.Symbol('z')
        summ = 0
        self.function = sp.integrate(self.function,y)
        self.d = "(("+self.d+")-x)"
        self.c = "("+self.c+")"
        self.function = self.function.replace("x", self.d)
        self.function = self.function.replace("x", self.c)
        self.function = sp.integrate(self.function,z)
        self.f = "(("+self.f+")-y)"
        self.e = "("+self.e+")"
        self.function = self.function.replace("z",self.f)
        self.function = self.function.replace("z",self.e)
        for i in range( 0, self.m ):
                z = self.arrxMid[i]
                e=eval(str(self.function))
                summ+=e*self.deltaX
        print(summ)"""
        
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")
        