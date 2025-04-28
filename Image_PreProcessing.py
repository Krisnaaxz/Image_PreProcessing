import cv2

#baca image dari file dengan path
image = cv2.imread("D:\SEMESTER 4\PENGANTAR PEMROSESAN DATA MULTIMEDIA\CODE-PPDM\Image_PreProcessing\kuda.jpeg")

#tampilkan image
cv2.imshow("kuda blue", image[:,:, 0]) #ambil channel biru
cv2.imshow("kuda green", image[:,:, 1]) #ambil channel hijau
cv2.imshow("kuda red", image[:,:, 2]) #ambil channel merah

#ambil channel warna BGR
print(image) #ambil semua channel warna BGR
print(image[:,:, 0]) #ambil channel biru
print(image[:,:, 1]) #ambil channel hijau
print(image[:,:, 2]) #ambil channel merah

#tunggu sampai tombol ditekan
cv2.waitKey()