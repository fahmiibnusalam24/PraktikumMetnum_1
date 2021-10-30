# Nama  : Fahmi Ibnu Salam
# NPM   : 2020102250004
# Kelas : TF3A4


import numpy as np
import matplotlib.pyplot as plt
from math import e #untuk memanggul bilangan eksponen natural (e)

def f(x):
    return e**x-5*x**2

def Df(x):
    return e**x-10*x

def newtonRaphson(x0,eps):
    step = 0
    print('\n\n*** ---METODE NEWTON RAPHSON--- ***')
    xn = x0
    for n in range(0,100):
        fxn=f(xn) 
        if abs(fxn) < eps:
            print('\n Akar Persamaan tersebut : %0.8f' % xn)
            return xn
        Dfxn=Df(xn)
        if Dfxn == 0:
            print('Solusi tidak ditemukan')
            return None
        xn=xn-(fxn/Dfxn)
        step = step + 1
        print('Interasi-%d, x = %0.8f dan f(x) = %0.8f' % (step, xn, f(xn)))
    print('Interasi maksimum, solusi tidak ditemukan')

x0 = float(input('x0: '))
eps = float(input('epsilon : '))
newtonRaphson(x0,eps)