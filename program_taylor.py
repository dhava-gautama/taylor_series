# Taylor Series
# This program will give you the taylor expansion series
# and it's corresponding value to the N-th terms
# Dhava Gautama
# Thanks to Bu Fitri, StackOverflow, GeeksforGeeks, SciPy Docs, JournalDev, Programiz
# https://github.com/dhava-stmkg/taylor_series
# Versi 1

import numpy as np
import sympy as sy
from sympy.functions import *
from numpy import math

# Factorial function
def factorial(n):
    return math.factorial(n)

# Define x as symbol using sympy lib
x = sy.Symbol('x')
a = sy.Symbol('a')

# Taylor approximation at x0 of the function f(x)
def taylor(fungsi, x0, n,nilai_x):
    pdkt = []
    i = 0
    p = 0
    while i <= n:
        # fungsi.diff(x,i) => Calculate i-th order derivative of the function on x
        # subs(x,x0) => Subs the value of x with x0
        p = p + (fungsi.diff(x,i).subs(x,x0))/(factorial(i))*(x-x0)**i
        i += 1
        pdkt.append(p.subs(x,nilai_x)) 
    return [p,pdkt];


# error_approach function
def error_approach(f, x0,nilai_x, acc_err, max_iter):
    for n in range(1,max_iter+1):
        func = taylor(f, x0, n, nilai_x)
        app_value = np.float(func[0].subs(x,nilai_x)) # Calculate the approx. value
        t_value = np.float(f.subs(x,nilai_x)) # Calculate the true value
        t_error = abs(app_value - t_value) # Calculate the true error
        t_r_error = abs((t_error/t_value)*100) # Calculate the relative true error
        # print(t_error)
        if t_error < acc_err:
            print('Nilai fungsi',f.subs(x,nilai_x),'dengan true error kurang dari',acc_err,'ditemukan setelah',n,'iterasi. Nilai error =',t_error)
            print('Nilai pendekatan fungsi',f.subs(x,nilai_x),'=',app_value)
            # print(func[0],func[1])
            return app_value
    print('Melebihi maksimum iterasi.')
    return None

# Taylor expansion
def pendekatan():
    f = eval(input('f(x) = '))
    x0 = eval(input('x0 = '))
    nilai_x = eval(input('x = '))
    n = eval(input('n = '))
    p = taylor(f, x0, n, nilai_x)
    pdkt = p[1]
    print('Ekspansi taylor pada orde n = '+str(n), "\n"+str(p[0]))
    if nilai_x != x:
        hasil_pendekatan = np.float(p[0].subs(x,nilai_x)) # Nilai pendekatan
        print('Approximate Value =', hasil_pendekatan)
        true_value = np.float(f.subs(x,nilai_x)) # Nilai sesungguhnya
        true_error = hasil_pendekatan - true_value # Nilai true error
        rel_true_error = abs(true_error/true_value)*100 # Nilai relative true error
        print('True Error =', true_error)
        print('Relative True Error =', rel_true_error,'%')
        pdkt = list(dict.fromkeys(pdkt)) # Menghapus nilai duplikat pada array
        pdkt.reverse() # Membalikan urutan array
        if 0 in pdkt: # Jika ditemukan nilai nol dalam array
            pdkt.remove(0) # Menghapus nilai nol
        if len(pdkt) >= 2: # Jika terdapat lebih dari sama dengan 2 elemen array maka approximate error ada 
            app_err = np.float(pdkt[0]-pdkt[1]) # Nilai approximate error
            rel_app_err = app_err/pdkt[0]*100 # Nilai relative approximate error
            print('Approximate Error =', app_err)
            print('Relative Approximate Error =', rel_app_err,'%')

# Approach the value of f(x) with certain true error limit
def aproaching_error():
    f = eval(input('f(x) = '))
    x0 = eval(input('x0 = '))
    nilai_x = eval(input('x = '))
    acc_err = eval(input('Acceptable true error value = '))
    # print(
    #    '''Mode iterasi 
    #    1. Terbatas (disarankan)
    #    2. Tak terbatas
    #    ''')
    max_iter = int(input('''Mode Iterasi
    1. Terbatas (disarankan)
    2. Tak terbatas
    Mode Iterasi : '''))
    if max_iter == 1:
        n = eval(input('Masukan batas iterasi'))
        error_approach(f, x0, nilai_x, acc_err, n)
    elif max_iter == 2:
        error_approach(f, x0, nilai_x, acc_err,9999999999999999999999)
    else: print("[!] lihat menu dong(o)")

def menu():
    print(
        '''
        ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        ;       TAYLOR SERIES       ;
        ;---------------------------;
        ; Author : Kang-dhava       ;
        ; Contact : t.me/dhavakun   ;
        ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        1. Taylor expansion
        2. Approach the value of f(x) with certain true error limit
        3. Exit
        '''
    )
    pilih=int(input('/Kang-Dhava: '))
    if pilih == 1:
        pendekatan()
    elif pilih == 2:
        aproaching_error()
    elif pilih == 3:
        exit('Sampai jumpa!')
    else: print("[!] lihat menu dong(o)");menu()
        
menu()
