#Caige Middaugh
#All Types of Integral Calculator
#Sympy is required I used the spyder editor from anaconda
#All files are required to be put in the same folder
import DoubleIntegralOptions
import SingleIntegral
import TripleIntegralOptions
from os import sys

def option1():
    print("Press E any time to Go Back")
    n = input("Enter number of dx or dy Squares: ")
    if n == "E":
        main()
    a = input("Enter starting point for x: ")
    if a == "E":
        main()
    b = input("Enter ending point for x: ")
    if b == "E":
        main()
    function = input("Enter Function(to find length of line enter 1): ")
    if function == "E":
        main()
    SingleIntegral.SIOption(n,a,b,function)
    main()
    
def option2():
    print("Press E To Go Back")
    m = input("Enter m(The amount of dx rectangle): ")
    if m == "E" :
        main()
    n = input("Enter n(The amount of dy rectangle): ")
    if n == "E" :
        main()
    a = input("Enter the Beginning point for x: ")
    if a == "E" :
        main()
    b = input("Enter the ending point for x: ")
    if b == "E" :
        main()
    c = input("Enter the beginning point for y: ")
    if c == "E" :
        main()
    d = input("Enter the ending point for y: ")
    if d == "E" :
        main()
    function = input("Enter the Function: ")
    if function == "E" :
        main()
    DoubleIntegralOptions.evaluateDoubleIntegral(m,n,a,b,c,d,function)
    main()
    
def option3():
    print("Press E To Go Back")
    m = input("Enter m(The amount of dx rectangle): ")
    if m == "E":
        main()
    n = input("Enter n(The amount of dy rectangle): ")
    if n == "E":
        main()
    p = input("Enter p(The amount of dz rectangle): ")
    if n == "E":
        main()
    a = input("Enter the Beginning point for x: ")
    if a == "E" :
        main()
    b = input("Enter the ending point for x: ")
    if b == "E" :
        main()
    c = input("Enter the beginning point for y: ")
    if c == "E" :
        main()
    d = input("Enter the ending point for y: ")
    if d == "E" :
        main()
    e = input("Enter the beginning point for z: ")
    if ( e == "E"):
        main()
    f = input("Enter the ending point for z: ")
    if ( f == "E"):
        main()
    function = input("Enter the Function: ")
    if function == "E" :
        main()
    order = input("What order to solve the integral?(dxdydz, etc)")
    if order == "E":
        main()
    TripleIntegralOptions.evaluateTripleIntegral(m,n,p,a,b,c,d,e,f,function, order)
    main()
        
def option4():
    print("\n\nAddition is +")
    print("Subtraction is -")
    print("Exponent(^) is ** Example: x**(5-y) in python is x^(5-y) in calculator")
    print("Multiplication is * ")
    print("Division is /")
    print("Modulus is %")
    print("Floor Division is //")
    print("Square Root is sqrt() Example: sqrt(x**(3)+y)")
    print("Cube Root use **(1/3) same for 4th Root **(1/4),etc")
    print("sin(),cos(),tan() can all be used but no inverses(yet?)")
    print("Raise to Power of Trig Function (cos(x))**2 NOT cos**2(x), same for tan and sin")
    print("You must use * any time you want to multiply Examples:")
    print("Good Example: x*y*z+2*x**(y-2*z)")
    print("Bad Example: xyz+2x^(y-2z)")
    print("Besides these make sure parenthesis are used properly on insert of functions")
    main()
    
def option5():
    print("Exiting")
    sys.exit(0)
    
def main():
    print("\nIf your new to Python Look at Library I explain some of the operators")
    print("\n1. Single Integral Calculator")
    print("2. Double Integral Calculator")
    print("3. Triple Integral Calculator")
    print("4. Library of Python Symbols(Have to use these)")
    print("5. Exit")
    option = int(input("Which option? "))
    
    if option == 1 :
        option1()
    elif option == 2 :
        option2()
    elif option == 3 :
        option3()
    elif option == 4 :
        option4()
    elif option == 5 :
        option5()
main()