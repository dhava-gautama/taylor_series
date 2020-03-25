# Taylor Series
# This program will give you the taylor expansion series and it's corresponding value to the N-th terms
# It also give you truncation error, true error, relative true error, approximate error, and relative approximate error
# Dhava Gautama
# Thanks to Allah, My Parets, Bu Fitri, StackOverflow, GeeksforGeeks, SciPy Docs, JournalDev, Programiz
# https://github.com/dhava-stmkg/taylor_series
# Versi 1.3

import numpy as np # Mengimport modul numpy.
import sympy as sy # Mengimport modul sympy.
from sympy.functions import * # Mengimport modul fungsi (sin, cos, tan, exp, ln, etc) dari modul sympy.
from math import factorial # Mengimport modul factorial dari modul math. 

# Define x as symbol using sympy lib
x = sy.Symbol('x')
c = sy.Symbol('c')

# Taylor approximation at x0 of the function f(x)
def taylor(fungsi, x0, n,nilai_x):
    pdkt = [] # Membuat array kosong
    deret = []
    i = 0 # Inisiasi nilai i = 0
    p = 0 # Inisiasi nilai p = 0
    while i <= n:
        # fungsi.diff(x,i) => Calculate i-th order derivative of the function on x
        # subs(x,x0) => Subs the value of x with x0
        p = p + (fungsi.diff(x,i).subs(x,x0))/(factorial(i))*(x-x0)**i # Looping fungsi sigma deret taylor
        i += 1 # Menambah nilai i
        pdkt.append(p.subs(x,nilai_x)) # Menambahkan nilai hasil pendekatan tiap iterasi ke array
        deret.append((fungsi.diff(x,i).subs(x,c))/(factorial(i))*(x-c)**i) # Menambahkan tiap suku ke array. Digunakan untuk mendapatkan truncation error
    return [p,pdkt,deret]; # Memberikan output hasil fungsi dalam bentuk array 


# error_approach function
def error_approach(f, x0,nilai_x, acc_err, n):
    i = 0 # Inisiasi nilai i = 0
    p = 0 # Inisiasi nilai p = 0
    t_value = np.float(f.subs(x,nilai_x))
    t_error = 1
    while i <= n:
        # f.diff(x,i) => Calculate i-th order derivative of the function on x
        # subs(x,x0) => Subs the value of x with x0
        p = p + (f.diff(x,i).subs(x,x0))/(factorial(i))*(x-x0)**i # Looping fungsi sigma deret taylor
        app_value = p.subs(x,nilai_x)
        t_error = abs(t_value - app_value) # Calculate the true error
        i += 1
        if t_error <= acc_err: #bila nilai true error sudah kurang dari nilai error yang dapat diterima
            print('Nilai pendekatan fungsi',f,'pada x =',nilai_x,'dengan true error kurang dari',acc_err,'ditemukan setelah',i,'iterasi. Nilai true error =',t_error)
            print('Nilai pendekatan fungsi',f.subs(x,nilai_x),'=',np.float(app_value))
            break
            return None
        if i >= n:
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
    deret = p[2]
    print('Ekspansi taylor pada orde n = '+str(n),'\n f(x) = ',p[0])
    print('Truncation error =',deret[-1])
    if nilai_x != x:
        hasil_pendekatan = np.float(p[0].subs(x,nilai_x)) # Nilai pendekatan
        print('Approximate Value =', hasil_pendekatan)
        true_value = np.float(f.subs(x,nilai_x)) # Nilai sesungguhnya
        true_error = abs(true_value - hasil_pendekatan) # Nilai true error
        rel_true_error = abs(true_error/true_value)*100 # Nilai relative true error
        print('Absolute True Error =', true_error)
        print('Relative True Error =', rel_true_error,'%')
        pdkt = list(dict.fromkeys(pdkt)) # Menghapus nilai duplikat pada array 
        pdkt.reverse() # Membalikan urutan array
        if 0 in pdkt: # Jika ditemukan nilai nol dalam array
            pdkt.remove(0) # Menghapus nilai nol dalam array
        if len(pdkt) >= 2: # Jika terdapat lebih dari sama dengan 2 elemen array maka approximate error ada 
            app_err = abs(np.float(pdkt[0]-pdkt[1])) # Nilai approximate error
            rel_app_err = app_err/pdkt[0]*100 # Nilai relative approximate error
            print('Absolute Approximate Error =', app_err)
            print('Relative Approximate Error =', rel_app_err,'%')

# Approach the value of f(x) with certain true error limit
def aproaching_error():
    f = eval(input('f(x) = '))
    x0 = eval(input('x0 = '))
    nilai_x = eval(input('x = '))
    acc_err = eval(input('Acceptable absolute true error value = '))
    max_iter = int(input('''Mode Iterasi
    1. Terbatas (disarankan)
    2. Tak terbatas
    Mode Iterasi : '''))
    if max_iter == 1:
        n = eval(input('Batas iterasi : '))
        error_approach(f, x0, nilai_x, acc_err, n)
    elif max_iter == 2:
        error_approach(f, x0, nilai_x, acc_err,9999999999999999999999)
    else: print("[!] mohon untuk membaca menu kembali(o)")

def menu():
    print(
        '''
        ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        ;       TAYLOR SERIES       ;
        ;---------------------------;
        ; Author : Kang-dhava       ;
        ; Contact : t.me/dhavakun   ;
        ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        1. Taylor expansion for an f(x) function
        2. Approach the value of f(x) with certain true error limit
        3. Exit
        
        Panduan penggunaan
        - Gunakan variabel x untuk fungsi
        - Pangkat ditulis sebagai ** . Cnth : x^2 ditulis x ** 2
        - Penulisan fungsi
            - e^x = exp(x)
            - Logaritma
                - Logaritma natural dapat ditulis : ln(x) atau log(x)
                - Logartima x dengan basis konstanta y : log(x,y)
            - Trigonometri
                - Untuk fungsi trigonometri ditulis : sin(x), cos(x), etc
                - Untuk invers beri huruf a pada depan fungsi, cnh : asin(x), acos(x), etc
        
        Note
        - Nilai approximate error diambil dari selisih nilai deret taylor pada n dan n-1, bila selisihnya 0 maka akan diambil selisih deret taylor pada n dan n-2 dan seterusnya
        
        '''
    )
    pilih=int(input('/Kang-Dhava: '))
    if pilih == 1:
        pendekatan()
    elif pilih == 2:
        aproaching_error()
    elif pilih == 3:
        exit('Sampai jumpa!')
    else: print("[!] mohon untuk membaca menu kembali(o)");menu()
        
menu()
