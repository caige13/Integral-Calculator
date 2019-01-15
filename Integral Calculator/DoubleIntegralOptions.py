import DOUBLEINTEGRALCLASS

def evaluateDoubleIntegral(m,n,a,b,c,d,function):     
    FunctionOf = False
    m = int(m)
    n = int(n)
    checkx = []
    checky = []
    checky = a.split("y")
    checky.append(b.split("y"))
    checkx = c.split("x")
    checkx.append(d.split("x"))
    
    if len(checky) > 2 or len(checkx) > 2 :
        FunctionOf = True
        
    if FunctionOf == True :
        FunctionOfY= False
        setting = 3
        if (len(checkx)>2):
            FunctionOfY=True
            a = float(a)
            b = float(b)
        else:
            c = float(c)
            d = float(d)
            
        DI3 = DOUBLEINTEGRALCLASS.DoubleIntegral(int(m),int(n),a,b,c,d,function,FunctionOfY,setting)
        if( FunctionOfY == True):
            DI3.setx()
            DI3.evaluateFunctionOfV()
        else:
            DI3.sety()
            DI3.evaluateFunctionOfV()
            
    else:   
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        
        if function == "1" :
            DI2 = DOUBLEINTEGRALCLASS.DoubleIntegral(m,n,a,b,c,d,"1",False,0)
            DI2.evaluateMidArea()        
        else:
            DI1 = DOUBLEINTEGRALCLASS.DoubleIntegral(m,n,a,b,c,d,function, False, 0)
            DI1.setx()
            DI1.sety()
            DI1.evaluateMid()

        stop = 0
        while ( stop ==0 ):
            option = input("Would you like to know the Lower Left, Upper Left, Lower Right or Upper Right values(Upper Right/Upper Left/etc) ")
            if option == "lower Left" or option == "Lower Left" or option == "lower left" or option=="Lower left":
                DI1.evaluateLLeft()
            elif option == "upper Left" or option == "Upper Left" or option == "upper left" or option=="Upper left":
                DI1.evaluateULeft()
            elif option == "lower Right" or option == "Lower Right" or option == "lower right" or option=="Lower right":
                DI1.evaluateLRight()
            elif option == "upper Right" or option == "Upper Right" or option== "upper right" or option=="Upper right":
                DI1.evaluateURight()
            else:
                stop = 1
    
