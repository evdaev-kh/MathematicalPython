import numpy as np
import sympy as sym
import matplotlib.pyplot as plt 
import math

def finite_diff(f, x, type="forward", error=0.01, static=True):
    """
    Goal: Calculate the derivative of a function at a range of x values using the forward diff. method

    Inputs:
        f       -- fuction given as a lambda
        x       -- a range of x values (domain) on which the function f is defined 
        type    -- indicates the type of finite difference (forward, backward, central)  
        error   -- represents the desired level of accuracy when determing stepsize 
        static  -- whether to use static or adaptive step
    """

 
    if (type == "backward"):
        g = lambda x, h:    (f(x) - f(x-h))/h
    elif (type == "central"):
        g = lambda x, h:    (f(x+h) - f(x-h))/(2*h)
        print(f"Using {type}") 
    else:
        g = lambda x, h:    (f(x+h) - f(x))/h  


    
    #h = 2*math.sqrt(error)
    h = (x[-1] - x[0])/len(x)
    D = []
    X = []
    x_ = x[0]
    if(not static):
        #Adaptive Step Size Method
        while x_ < x[-1]:
                
            h1 = error
            h2 = error/2

            dx1 = g(x_, h1)
            dx2 = g(x_, h2)
            
            while(abs(dx1 - dx2)>= error):
                h1 = h2
                h2 = h2/2

                dx1 = g(x_, h1)
                dx2 = g(x_, h2)
            
            D.append(dx2)
            X.append(x_)
            x_ = x_ + h2
    else:
        #Static Step Size Method
        for x_ in x:
            dx = g(x_, h)
            D.append(dx)
            X.append(dx)
    
    return D, X


x = sym.Symbol('x')
#f = sym.exp(-0.1*x)*sym.cos(x)
#f = sym.log(x)
f = x**4 - 2*x**2

df = sym.diff(f)
f = sym.lambdify(x, f)
df = sym.lambdify(x, df)

x_vals = np.linspace(-2, 2, 500)
D_adaptive, X_ad = finite_diff(f, x_vals, "central", 0.5, False)
D_static, X_stat = finite_diff(f, x_vals, "central", 0.5, True)

plt.rc('grid', linestyle=':', color='black', linewidth=2)
plt.figure(figsize=(20,18), dpi=100)
timeDelay = 0.75
plt.plot(x_vals, f(x_vals), label=f'f={sym.exp(-0.1*x)*sym.cos(x)}')
plt.pause(timeDelay)

plt.plot(X_ad, D_adaptive, label='Adaptive step size appr.')
plt.pause(timeDelay)

plt.plot(x_vals, D_static, label='Static step appr.')
plt.pause(timeDelay)

plt.plot(x_vals, df(x_vals), label='Actual derivative')
plt.pause(timeDelay)

plt.plot()
plt.legend()
plt.show()