"""class DoubleIntegral:
    USED TO CALCULATE DOUBLE INTEGRALS - CAIGE MIDDAUGH
    def __init__(self, m, n,a,b,c,d,function):
        self.m=m
        self.n=n
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.function=function
        self.deltaX=(b-a)/m
        self.deltaY=(d-c)/n
        self.deltaA=self.deltaX*self.deltaY
        self.y=[]
        self.arryLeft=[]
        self.arryRight=[]
        self.arryMid=[]
        self.x=[]
        self.arrxLeft=[]
        self.arrxMid=[]
        self.arrxRight=[]

    def setx(self):
        for i in range (0,self.m+1):
            if i == 0 :
                self.x.append(self.a)
            else:
                self.x.append(self.x[i-1]+self.deltaX)
        
        for i in range (0,self.m):
            if i == 0 :
                self.arrxLeft.append(self.a)
            else:
                self.arrxLeft.append(self.arrxLeft[i-1]+self.deltaX)
        
        for i in range (1,self.m+1):
            print(i)
            if i == 1 :
                self.arrxRight.append(self.a+self.deltaX)
            else:
                self.arrxRight.append(self.arrxRight[i-2]+self.deltaX)
        
        for i in range (1,self.m+1):
            middle=self.x[i-1]+self.x[i]
            middle/=2
            self.arrxMid.append(middle)

    def Sety(self):
        for i in range (0,self.n+1):
            if i == 0 :
                self.y.append(self.c)
            else:
                self.y.append(self.y[i-1]+self.deltaY)
        
        for i in range (0,self.n):
            if i == 0 :
                self.arryLeft.append(self.c)
            else:
                self.arryLeft.append(self.arryLeft[i-1]+self.deltaY)
        
        for i in range (1,self.n+1):
            if i == 1 :
                self.arryRight.append(self.c+self.deltaY)
            else:
                self.arryRight.append(self.arryRight[i-2]+self.deltaY)
        
        for i in range (1,self.n+1):
            middle=self.y[i-1]+self.y[i]
            middle/=2
            self.arryMid.append(middle)

    def evaluateMid(self):
        summ=0
        for i in range(0, self.n):
            x = self.arrxMid[i]
            print(i)
            for j in range ( 0, self.m ):
                y= self.arryMid[j]
                print("Comparing", x, " and ", y)
                e = eval(self.function)
                print(e)
                summ += e*self.deltaA
        print("Mid Point: ",summ)


    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")
"""
def main():
    print("HU")
    n = int(input("Enter m(The amount of dx rectangle): "))
    m = int(input("Enter n(The amount of dy rectangle): "))
    a = int(input("Enter the Beggining point for x: "))
    b = int(input("Enter the ending point for x: "))
    c = int(input("Enter the beginning point for y: "))
    d = int(input("Enter the ending point for y: "))
    function = input("Enter the Function: ")
    print (n,m,a,b,c,d,function)
    """doubleint1 = DoubleIntegral(m,n,a,b,c,d,function)
    doubleint1.setx()
    doubleint1.sety()
    doubleint1.evaluateMid()"""
"""
creating arrays to hold the values of x* and y*. This is one solution.
"""
"""
x = [0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1]
y = [0,.2,.4,.6,.8,1,1.2,1.4,1.6,1.8,2]

"""
"""
nesting the for loops to make the each x value interact with each y value.
"""
"""for i in range ( 0, m ):
    for j in range ( 0, n ):
        print( "comparing x ", i, "with y ", j)
        a=math.sqrt(x[i]**3+y[j]**3)
        print("a " , j , ":  ", a)
        func = math.sin(a);
        print("func: " , j , ":  " , func)
        summ += func*deltaA;

print(summ);
"""
