import cv2
import numpy as np


#baca image dari file dengan path
image = cv2.imread("D:\SEMESTER 4\PENGANTAR PEMROSESAN DATA MULTIMEDIA\CODE-PPDM\Image_PreProcessing\kuda.jpeg")

blue = image[:,:, 0] #ambil channel biru
green = image[:,:, 1] #ambil channel hijau
red = image[:,:, 2] #ambil channel merah

# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert to grayscale using library OpenCV
# cv2.imshow("kuda gray", image_gray) #tampilkan image grayscale

#menyiapkan variabel untuk menyimpan ukuran image grayscale
jbaris = len(image) #jumlah baris
lbaris = len(image[0]) #jumlah kolom

image_gray = np.zeros((jbaris, lbaris)) #inisialisasi variabel image grayscale

#melakukan konversi ke grayscale
for i in range(len(image)):
    for j in range(len(image[0])):
        image_gray[i][j] = round(0.299 * red[i][j] + 0.587 * green[i][j] + 0.114 * blue[i][j]) #rumus konversi ke grayscale

image_gray = image_gray.astype(np.uint8) #convert to uint8

cv2.imshow("kuda gray", image_gray) #tampilkan image grayscale
print(image_gray) #print semua matriks grayscale

cv2.waitKey(0) #tunggu sampai tombol ditekan