# FaHmi Ibnu Salam
# 202010225004
# TF3A4


import numpy as np

# membaca jumlah titik data
n = int (input('Masukkan jumlah titik data: '))

# membuat array ukuran n x m dan inisiasi 
x = np.zeros((n))
y = np.zeros((n))

# membaca titik data
print ('Masukkan data x dan y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i] = float(input( 'y['+str(i)+']='))
    
# membaca interpolasi titik 

xp = float(input('Masukkan x yang di inginkan: '))

# inisialisasi interpolasi

yp = 0

# implementasai interpolasi Lagrange
for i in range(n):
    
    p = 1
    
    for j in range(n):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
        
    yp = yp + p * y[i]
        
   
# Displaying output

print('Nilai Interpolasi untuk %.3f adalah %.3f.' % (xp, yp))
        
     