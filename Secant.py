#Nama   : Akmal Maulfi Anwar
#NPM    : 20201022504
#Kelas  : TF3A4


import numpy as np
import matplotlib.pyplot as plt
from math import e

def f(x):
    return e**x-5*x**2

def Secant(x0,x1,eps, N):
    step = 1
    coundition = True
    while coundition:
        if f(x0) == f(x1):
            print ('Solusi tidak ditemukan')
            break

        x2 = x1 - ((f(x1)*(x1-x0))/(f(x1)-f(x0)))
        print('Interasi-%d, x = %0.8f dan f(x) = %0.8f' % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1

        if step > N:
            print('Divergen')
            break
        coundition = abs(f(x2)) > eps
    print('\n Akar Persamaan tersebut : %0.8f' % x2)

x0 = float(input('x0: '))
x1 = float(input('x1: '))
N = int(input('Max Iter: '))
eps =float(input('epsilon: '))
Secant(x0,x1,eps, N)