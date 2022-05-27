import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import math
import random

def secant(f, a, b, error):
    """
    Description: the bisection method for finding the roots of the equation using halving the interval method

    Inputs:
        f       - a function (defined as a lambda)
        a       - the left end of the interval
        b       - the right end of the interval
        error   - the length of the desired interval
    
    Output:
        the x value of the root
    
    Assumption/Notes:
        - the function must be a 2-dimensional one
        - there must be a root between the endpoints [a,b] otherwise the function fails
        - we calculate the number of iterations needed to reach a desired error value prescribed by the analytical formula
                ln( (b-a)/error ) / ln(2) - 1
    """

    if(f(a)*f(b) >= 0):
        print("The interval defined by [" + a + ", " + b + "] has no roots!")
        return None
    
    #calculate the number of iterations
    #N =  int (math.log((b-a)/error, math.e) / math.log(2, math.e) - 1)
    #print("Number of iterations required for %3.3f error is %d" % (error, N))
    x = 0
    iter = 0
    while(abs(a-b) >= error):
        iter +=1
        print("Iteration %d \n" %(iter))
        f_a = f(a)
        f_b = f(b)
        x = a - f_a*((b-a)/(f_b - f_a))
        f_x = f(x)
        if(f(a)*f_x < 0):
            b = x
        elif (f(b)*f_x < 0):
            a = x
        elif (f_x == 0):
            return x
        else:
            print("Bisection method failed!")
    return x

def bisection(f, a, b, error):
    """
    Description: the bisection method for finding the roots of the equation using secant lines

    Inputs:
        f       - a function (defined as a lambda)
        a       - the left end of the interval
        b       - the right end of the interval
        error   - the length of the desired interval
    
    Output:
        the x value of the root
    
    Assumption/Notes:
        - the function must be a 2-dimensional one
        - there must be a root between the endpoints [a,b] otherwise the function fails
        - we calculate the number of iterations needed to reach a desired error value prescribed by the analytical formula
                ln( (b-a)/error ) / ln(2) - 1
    """

    if(f(a)*f(b) >= 0):
        print("The interval defined by [" + a + ", " + b + "] has no roots!")
        return None
    
    #calculate the number of iterations
    N =  int (math.log((b-a)/error, math.e) / math.log(2, math.e) - 1)
    print("Number of iterations required for %3.3f error is %d" % (error, N))
    mid_point = 0
    iter = 0
    for i in range(1, N+1):
        iter +=1
        print("Iteration %d \n" %(iter))
        mid_point = (a+b)/2
        f_m = f(mid_point)
        if(f(a)*f_m < 0):
            b = mid_point
        elif (f(b)*f_m < 0):
            a = mid_point
        elif (f_m == 0):
            return mid_point
        else:
            print("Bisection method failed!")
    return (a+b)/2

def NewtonMethod(f, d_f, error, x0):
    """
    Description: The famous Newton's method for finding/approximating the roots of an equation

    Inputs:
        f       - the function of interest
        d_f     - the derivative of the function
        error   - desired level of error/accuracy
        x0      - the starting/initial x point
    
    Notes:
        - Newton's method is an example of an unbounded algorithm for fidning the roots of an equation
        - It is relatively faster than the bounded algorithms for finding a root but it relies on a initial value
            i.e. it could fail if the initial value is not picked right
    """
    iter = 0
    while(abs(f(x0)) >= error):
        print("Iteration %d\n" %(iter))
        iter +=1
        x0 = x0 - (f(x0)/d_f(x0))
        print("x0: %3.3f" % (x0))
        if (d_f(x0) == 0):
            print("Zero derivative: can't proceed")
            return None
    return x0
            

x_vals = np.linspace(-5,5,200)
f = lambda x: 0.5*x**3 - 5*x - 1
d_f = lambda x: 1.5*x**2 - 5
y_quad = f(x_vals)
plt.plot(x_vals, y_quad)
plt.show()

root1 = NewtonMethod(f, d_f, 0.0001, -4.5)
print(root1, f(root1))

g = lambda x: math.cos(x)
d_g = lambda x: -math.sin(x)
plt.plot(x_vals, np.cos(x_vals))
plt.show()
root2 = NewtonMethod(g, d_g, 0.01, 3)
print(root2, g(root2))
# root2 = bisection(f, -2, 0, 0.001)
# print(root2, f(root2))
# root3 = bisection(f, 2,4, 0.001)
# print(root3, f(root3))

# x = sym.Symbol('x')
# g = x**2 -3*x + 1
# #y_g = [g(x_) for x_ in x_vals]
# d_g = g.diff(x)
# print(d_g)
