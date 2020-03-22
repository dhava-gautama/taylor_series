import sympy as sy
from sympy.functions import *
from numpy import math

# Factorial function
def factorial(n):
    return math.factorial(n)

# Define x as symbol using sympy lib
x = sy.Symbol('x')

# Input the function
f = sin(x)

# Fungsi untuk mengekspansi deret taylor
def taylor(fungsi, a, n):
    i = 0
    p = 0
    turunan = []
    while i <= n:
        # fungsi.diff(x,i) => Calculate i-th order derivative of the function on x
        # subs(x,x0) => Subs the value of x with x0
        p = p + (fungsi.diff(x,i).subs(x,a))/(factorial(i))*(x-x0)**i
        turunan.append(fungsi.diff(x,i))
        print('Turunan ke-'+str(i),'=',turunan[i])
        i += 1
    return p

# Menjalankan fungsi deret taylor
taylor(f,0,10)
