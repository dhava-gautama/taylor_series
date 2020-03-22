# Taylor Series
# This program will give you the taylor expansion series
# and it's corresponding value to the N-th terms
# Dhava Gautama
# Thanks to Allah, My Parents, Bu Fitri, StackOverflow, GeeksforGeeks, SciPy Docs, JournalDev, Programiz
# https://github.com/dhava-stmkg/taylor_series
# Versi 0.1.3

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
    tailor = []
    while i <= n:
        # fungsi.diff(x,i) => Calculate i-th order derivative of the function on x
        # subs(x,x0) => Subs the value of x with x0
        p = p + (fungsi.diff(x,i).subs(x,x0))/(factorial(i))*(x-x0)**i
        tailor.append(p.subs(x,nilai_x))
        i += 1
    hasil_pendekatan = np.float(p.subs(x,nilai_x))
    true_value = np.float(fungsi.subs(x,nilai_x))
    true_error = np.float(true_value-hasil_pendekatan)
    relative_true_error = np.float(true_error/true_value*100)
    # Diperlukan untuk mendapatkan nilai approx-error
    tailor = list(dict.fromkeys(tailor)) # Menghapus nilai duplikat pada array
    tailor.reverse() # Membalikan urutan array
    if 0 in tailor: # Jika ditemukan nilai nol dalam array
        tailor.remove(0) # Menghapus nilai nol
    # Menghitung nilai approx error
    app_err = np.float(tailor[0]-tailor[1]) # Nilai approximate error
    rel_app_err = app_err/tailor[0]*100 # Nilai relative approximate error
    return [hasil_pendekatan,true_value,true_error,relative_true_error,app_err,rel_app_err]

# Dekati sin(x) ketika x0=0, dan x=1 pada iterasi ke n=10 masukan ke kamar gas
gas = taylor(f, 0, 10, 1)
print('Nilai Pendekatan =',gas[0])
print('Nilai True Value =',gas[1])
print('Nilai True Error =',gas[2])
print('Nilai Relative True Error =',gas[3],'%')
print('Nilai Approximate Error =',gas[4])
print('Nilai Relative Approximate Error =',gas[5],'%')
