import cv2
import numpy as np
import matplotlib.pyplot as plt

citra = cv2.imread("kuda.jpeg", 0)  #Membaca citra gambar dalam grayscale
Histogram = cv2.calcHist([citra], [0], None, [256], [0, 256])  #Menghitung histogram citra

plt.plot(Histogram)  #Menampilkan histogram citra
plt.title("Histogram")
plt.title("Citra Kuda Grayscale")
plt.xlabel("Pixel Value")
plt.ylabel("Frekuensi")
plt.show()  #Menampilkan histogram citra

#Perhitungan Statistik Histogram
mean = np.mean(citra)
var = np.var(citra)
std = np.std(citra)

print(f'Rata-rata: {mean:.2f}')
print(f'Variansi: {var:.2f}')
print(f'Standar Deviasi: {std:.2f}')

# Analisis jenis citra berdasarkan mean dan standar deviasi
if mean < 85:
    brightness = "Citra Gelap"
elif mean > 170:
    brightness = "Citra Terang"
else:
    brightness = "Citra Normal"

if std > 70:
    contrast = "Citra Kontras Tinggi"
else:
    contrast = "Citra Kontras Rendah"

print(f'Analisis Kecerahan: {brightness}')
print(f'Analisis Kontras: {contrast}')

#Menampilkan gambar citra
cv2.imshow("kuda", citra)
cv2.waitKey(0)