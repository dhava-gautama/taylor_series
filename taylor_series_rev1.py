# Taylor Series
# This program will give you the taylor expansion series
# and it's corresponding value to the N-th terms
# Dhava Gautama
# Thanks to Allah, My Parents, Bu Fitri, StackOverflow, GeeksforGeeks, SciPy Docs, JournalDev, Programiz
# https://github.com/dhava-stmkg/taylor_series
# Versi 0.1.2

import numpy as np
import sympy as sy
from sympy.functions import sin, exp, ln
from numpy import math

# Factorial function
def factorial(n):
    return math.factorial(n)

# Define x as symbol using sympy lib
x = sy.Symbol('x')
# Input the function
f = sin(x)

# Taylor approximation at x0 of the function f(x)
def taylor(fungsi, x0, n,nilai_x):
    i = 0
    p = 0
    while i <= n:
        # fungsi.diff(x,i) => Calculate i-th order derivative of the function on x
        # subs(x,x0) => Subs the value of x with x0
        p = p + (fungsi.diff(x,i).subs(x,x0))/(factorial(i))*(x-x0)**i
        i += 1
    hasil_pendekatan = np.float(p.subs(x,nilai_x))
    true_value = np.float(fungsi.subs(x,nilai_x))
    true_error = np.float(hasil_pendekatan-true_value)
    relative_true_error = np.float(true_error/true_value*100)
    return [hasil_pendekatan,true_value,true_error,relative_true_error]

# Dekati sin(x) ketika x0=0, dan x=1 pada iterasi ke n=10
gas = taylor(f, 0, 10, 1)
print('Nilai Pendekatan =',gas[0])
print('Nilai True Error =',gas[2])
print('Nilai Relative True Error =',gas[3],'%')
