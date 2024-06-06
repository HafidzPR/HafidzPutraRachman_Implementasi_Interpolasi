# IMPLEMENTASI INTERPOLASI - METODE POLINOMIAL LAGRANGE + NEWTON
#=======================================================

# HAFIDZ PUTRA RACHMAN ~ (21120120140096)
# METODE NUMERIK (A)
#=======================================================

import numpy as np
import matplotlib.pyplot as plt

#=======================================================

# Fungsi Polinomial Lagrange
def polinomial_lagrange(x, y, x_new):
  total = 0
  n = len(x)
  for i in range(n):
    xi, yi = x[i], y[i]
    def L(i):
      terms = [((x_new - x[j]) / (xi - x[j])) for j in range(n) if j != i]
      return np.prod(terms, axis=0)
    total += yi * L(i)
  return total

#=======================================================

# Fungsi Polinomial Newton
def polinomial_newton(x, y, x_new):
  def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y
    for j in range(1, n):
      for i in range(n-j):
        coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])
    return coef[0, :]
  
  def newton_poly(coef, x_data, x_new):
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1, n+1):
      p = coef[n-k] + (x_new - x_data[n-k]) * p
    return p
  
  # Kalkulasi koefisien deivided_diff
  coef = divided_diff(x, y)
  # Kalkulasi nilai polinom di x_new
  return newton_poly(coef, x, x_new)

#=======================================================

# Pengujian Nilai Data dari data yang telah diberikan
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Pengujian Implementasi Polinomial Lagrange + Newton
x_new = np.linspace(5, 40, 100)
y_lagrange = polinomial_lagrange(x, y, x_new)
y_newton = polinomial_newton(x, y, x_new)

# Plot bentuk dan dimensi grafil dari hasil interpolasi nilai data
fig, axs = plt.subplots(1, 2, figsize=(10, 5), num='Grafik Implementasi Interpolasi     ----------->     HAFIDZ PUTRA RACHMAN ~ (21120120140096) ~ METODE NUMERIK (A)')

# Judul besar dan data NAMA/NIM
plt.suptitle('IMPLEMENTASI INTERPOLASI', fontsize=20, fontweight='bold', y=1)
plt.figtext(0.5, 0.95, '_________________________________', ha='center', va='center', fontsize=20, fontweight='bold')
plt.figtext(0.5, 0.88, '[HAFIDZ PUTRA RACHMAN]\n[21120120140096]', ha='center', va='center', fontsize=10, color='purple')

#=======================================================

# Tampilan Grafik = Interpolasi Lagrange
axs[0].plot(x, y, 'ro', label='Data Asli')
axs[0].plot(x_new, y_lagrange, 'b-', label='Interpolasi Lagrange')
axs[0].set_title('Polinomial Lagrange', fontweight='bold', color='blue')
axs[0].set_xlabel('Tegangan (kg/mm^2)')
axs[0].set_ylabel('Waktu Patah (jam)')
axs[0].legend()

# Tampilan Grafik = Interpolasi Newton
axs[1].plot(x, y, 'bo', markersize=5, label='Data Asli')
axs[1].plot(x_new, y_newton, 'r-', label='Interpolasi Newton')
axs[1].set_title('Polinomial Newton', fontweight='bold', color='red') 
axs[1].set_xlabel('Tegangan (kg/mm^2)')
axs[1].legend()

#=======================================================

# Menampilkan Gambar Grafik dan meranpingkannya agar lebih rapih
plt.tight_layout()
plt.show()