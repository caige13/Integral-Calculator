#There is so much logic used for triple integrals compared to the others
#almost makes me wonder if there is a better way
import TripleIntegralClass
from os import sys

def evaluateTripleIntegral(m,n,p,a,b,c,d,e,f,function, order):
    FunctionOfz = False
    FunctionOfzwithxy = False
    FunctionOfzwithy = False
    FunctionOfzwithx = False
    FunctionOfx=False
    FunctionOfxwithyz = False
    FunctionOfxwithy = False
    FunctionOfxwithz = False
    FunctionOfy = False
    FunctionOfywithxz = False
    FunctionOfywithx = False
    FunctionOfywithz = False
    integerx = False
    integerxwithy=False
    integerxwithz=False
    integery=False
    integerywithx = False
    integerywithz = False
    integerz=False
    integerzwithx = False
    integerzwithy = False
    FunctionOf2 = False
    deltaX=0
    deltaY=0
    deltaZ=0
    m = int(m)
    n = int(n)
    p = int(p)
    
    chararrayx = list(a)
    chararrayx2 = list(b)
    print(chararrayx)
    for i in range(0,len(chararrayx)):
        if chararrayx[i] == "y":
            integerxwithy = True
        elif chararrayx[i] == "z":
            integerxwithz = True
        elif integerxwithz == True and integerxwithy == True:
            break
    for i in range(0,len(chararrayx2)):
        if integerxwithz == True and integerxwithy == True:
            break
        elif chararrayx2[i] == "y":
            integerxwithy = True
        elif chararrayx2[i] == "z":
            integerxwithz = True
    if integerxwithy == True and integerxwithz == True:
        FunctionOfxwithyz = True
        FunctionOfx = True
    elif integerxwithy == True and integerxwithz == False:
        FunctionOfxwithy = True
        FunctionOfx = True
    elif integerxwithy == False and integerxwithz == True:
        FunctionOfxwithz = True
        FunctionOfx = True
    else:
        integerx = True
        a = float(a)
        b = float(b)
    chararrayx=[]
    chararrayx2=[]
    
    chararrayy = list(c)
    chararrayy2 = list(d)
    for i in range(0,len(chararrayy)):
        if chararrayy[i] == "x":
            integerywithx = True
        elif chararrayy[i] == "z":
            integerywithz = True
        elif integerywithx == True and integerywithz == True:
            break
    for i in range(0,len(chararrayy2)):
        if integerywithx == True and integerywithz == True:
            break
        elif chararrayy2[i] == "x":
            integerywithx = True
        elif chararrayy2[i] == "z":
            integerywithz = True
    if integerywithx == True and integerywithz == True:
        FunctionOfywithxz = True
        FunctionOfy = True
    elif integerywithx ==True and integerywithz == False:
        FunctionOfywithx = True
        FunctionOfy = True
    elif integerywithx == False and integerywithz == True:
        FunctionOfywithz = True
        FunctionOfy=True
    else:
        integery = True
        c = float(c)
        d = float(d)
    chararrayy = []
    chararrayy2 = []
    
    chararrayz = list(e)
    chararrayz2 = list(f)
    for i in range(0,len(chararrayz)):
        if chararrayz[i] == "x":
            integerzwithx = True
        elif chararrayz[i] == "y":
            integerzwithy = True
        elif integerzwithy == True and integerzwithx == True:
            break
    for i in range(0,len(chararrayz2)):
        if integerzwithy == True and integerzwithx == True:
            break
        elif chararrayz2[i] == "x":
            integerzwithx = True
        elif chararrayz2[i] == "y":
            integerzwithy = True
    if integerzwithx == True and integerzwithy == True:
        FunctionOfzwithxy = True
        FunctionOfz=True
    elif integerzwithx == False and integerzwithy == True:
        FunctionOfzwithy = True
        FunctionOfz = True
    elif integerzwithx ==True and integerzwithy == False:
        FunctionOfzwithx = True
        FunctionOfz = True
    else:
        integerz = True
        e = float(e)
        f = float(f)
    chararrayz = []
    chararrayz2 = []
        
    if integerx == False and integery == False and integerz == False:
        print("Cannot have 3 different functions as parameters")
        sys.exit(0)
    elif integerx == False and integery == False:
        FunctionOf2 = True
    elif integerx == False and integerz == False:
        FunctionOf2 = True
    elif integery == False and integerz == False:
        FunctionOf2 = True
        
    if FunctionOfy == True or FunctionOfz == True or FunctionOfx == True:
        if FunctionOf2 == True:
            if FunctionOfx == True and FunctionOfy == True:
                deltaZ = (f-e)/p
                TI1 = TripleIntegralClass.TripleIntegral(m,n,p,a,b,c,d,e,f,function,deltaX,deltaY,deltaZ)
                TI1.setz()
                if order == "dx dy dz" or order == "dxdydz" or order == "dx dydz" or order == "dxdy dz":
                    function = TI1.getdx()
                    TI1.setFunction(function)
                    function = TI1.getdy()
                    TI1.setFunction(function)
                    TI1.getSingleNumericalz()
                elif order == "dy dx dz" or order == "dydxdz" or order == "dy dxdz" or order == "dydx dz":
                    function = TI1.getdy()
                    TI1.setFunction(function)
                    function = TI1.getdx()
                    TI1.setFunction(function)
                    TI1.getSingleNumericalz()
            elif FunctionOfx == True and FunctionOfz == True:
                deltaY = (d-c)/n
                TI2 = TripleIntegralClass.TripleIntegral(m,n,p,a,b,c,d,e,f,function,deltaX,deltaY,deltaZ)
                TI2.sety()
                if order == "dx dz dy" or order == "dxdzdy" or order == "dx dzdy" or order == "dxdz dy":
                    function = TI2.getdx()
                    TI2.setFunction(function)
                    function = TI2.getdz()
                    TI2.setFunction(function)
                    TI2.getSingleNumericaly()
                elif order == "dz dx dy" or order == "dzdxdy" or order == "dz dxdy" or order == "dzdx dy":
                    function = TI1.getdz()
                    TI2.setFunction(function)
                    function = TI1.getdx()
                    TI2.setFunction(function)
                    TI2.getSingleNumericaly()
            elif FunctionOfy == True and FunctionOfz == True:
                deltaX = (b-a)/m
                TI3 = TripleIntegralClass.TripleIntegral(m,n,p,a,b,c,d,e,f,function,deltaX,deltaY,deltaZ)
                TI3.setx()
                if order == "dy dz dx" or order == "dydzdx" or order == "dy dzdx" or order == "dydz dx":
                    function = TI3.getdy()
                    TI3.setFunction(function)
                    function = TI3.getdz()
                    TI3.setFunction(function)
                    TI3.getSingleNumericalx()
                elif order == "dz dy dx" or order == "dzdydx" or order == "dz dydx" or order == "dzdy dx":
                    function = TI3.getdz()
                    TI3.setFunction(function)
                    function = TI3.getdy()
                    TI3.setFunction(function)
                    TI3.getSingleNumericalx()
                    
        else:
            if FunctionOfy == True:
                deltaX = (b-a)/m
                deltaZ = (f-e)/p
                TI4 = TripleIntegralClass.TripleIntegral(m,n,p,a,b,c,d,e,f,function,deltaX,deltaY,deltaZ)
                TI4.setx()
                TI4.setz()
                if order == "dy dz dx" or order == "dydzdx" or order == "dy dzdx" or order == "dydz dx" or order == "dy dx dz" or order == "dydxdz" or order == "dy dxdz" or order == "dydx dz":
                    function = TI4.getdy()
                    TI4.setFunction(function)
                    TI4.getDoubleNumericalxz()
                elif order == "dx dy dz" or order == "dxdydz" or order == "dx dydz" or order == "dxdy dz":
                    function = TI4.getdx()
                    TI4.setFunction(function)
                    function = TI4.getdy()
                    TI4.setFunction(function)
                    TI4.getSingleNumericalz()
                elif order == "dz dy dx" or order == "dzdydx" or order == "dz dydx" or order == "dzdy dx":
                    function = TI4.getdz()
                    TI4.setFunction(function)
                    function = TI4.getdy()
                    TI4.setfunction(function)
                    TI4.getSingleNumericalx
            elif FunctionOfz == True:
                deltaX = (b-a)/m
                deltaY = (d-c)/n
                TI5 = TripleIntegralClass.TripleIntegral(m,n,p,a,b,c,d,e,f,function,deltaX,deltaY,deltaZ)
                TI5.setx()
                TI5.sety()
                if order == "dz dy dx" or order == "dzdydx" or order == "dz dydx" or order == "dzdy dx" or order == "dz dy dx" or order == "dzdxdy" or order == "dz dxdy" or order == "dzdx dy":
                    function = TI5.getdz()
                    TI5.setFunction(function)
                    TI5.getDoubleNumericalxy()
                elif order == "dy dz dx" or order == "dydzdx" or order == "dy dzdx" or order == "dydz dx":
                    function = TI5.getdy()
                    TI5.setFunction(function)
                    function = TI5.getdz()
                    TI5.setfunction(function)
                    TI5.getSingleNumericalx
                elif order == "dx dz dy" or order == "dxdzdy" or order == "dx dzdy" or order == "dxdz dy":
                    function = TI5.getdx()
                    TI5.setFunction(function)
                    function = TI5.getdz()
                    TI5.setfunction(function)
                    TI5.getSingleNumericaly
            elif FunctionOfx == True:
                deltaY = (b-a)/n
                deltaZ = (f-e)/p
                TI6 = TripleIntegralClass.TripleIntegral(m,n,p,a,b,c,d,e,f,function,deltaX,deltaY,deltaZ)
                TI6.sety()
                TI6.setz()
                if order == "dx dy dz" or order == "dxdydz" or order == "dx dydz" or order == "dxdy dz" or order == "dx dy dz" or order == "dxdzdy" or order == "dx dzdy" or order == "dxdz dy":
                    function = TI6.getdz()
                    TI6.setFunction(function)
                    TI6.getDoubleNumericalxy()
                elif order == "dy dx dz" or order == "dydxdz" or order == "dy dxdz" or order == "dydx dz":
                    function = TI6.getdy()
                    TI6.setFunction(function)
                    function = TI6.getdx()
                    TI6.setfunction(function)
                    TI6.getSingleNumericalz
                elif order == "dz dx dy" or order == "dzdxdy" or order == "dz dxdy" or order == "dzdx dy":
                    function = TI6.getdz()
                    TI6.setFunction(function)
                    function = TI6.getdx()
                    TI6.setfunction(function)
                    TI6.getSingleNumericaly
    else:
        if function == "1":
            side1 = b-a
            side2 = d-c
            side3 = f-e
            volume = side1*side2*side3
            print(volume)
        else:
            deltaX = (b-a)/m
            deltaY = (d-c)/n
            deltaZ = (f-e)/p
            TI7 = TripleIntegralClass.TripleIntegral(m,n,p,a,b,c,d,e,f,function,deltaX,deltaY,deltaZ)
            TI7.setx()
            TI7.sety()
            TI7.setz()
            TI7.getTripleNumerical276()