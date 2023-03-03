import os #digunakan untuk menghapur=t output sebelumnya, agar tampilan terlihat rapih
from random import randint #digunakan untuk mengimport angka- anka random yang akan di sorting nanti
os.system('cls')

'''
yang pertama ada fungsi sorting dengan jenis merge sort
'''

def mergesort(data):
    if len(data) > 1: 
        mid = len(data) // 2 #menyatakan nilai tengah dimana dibagi 2 untuk menentukannya, apabila nilai nya angka desimal 
                             #maka akan dibulatkan kebawah
        left_data = data[:mid] #menyatakan nilai kiri, dimana indeks yang diambil yaitu dari tengah  ke kiri
        right_data = data[mid:]  #menyatakan nilai kanan, dimana indeks yang diambil yaitu dari tengah  ke kanan


        mergesort(left_data) #memanggil fungsi mergesort untuk data kiri
        mergesort(right_data) #memanggil fungsi mergesort untuk data kanan
        
         
        i = j = k=0 #menyatakan bahwa indeks untuk array kiri, kanan, dan indeks untuk penggabungannya sama dengan 0
        

        while i < len(left_data) and j < len (right_data): 
            if left_data[i] < right_data[j]:
                data[k]= left_data[i]
                i += 1 
                k += 1

            else:
                data[k] = right_data[j]
                j += 1
                k += 1

        while i < len(left_data):
            data[k] = left_data[i]
            i += 1
            k += 1

        
        while j < len(right_data):
            data[k] = right_data[j]
            j += 1
            k += 1

print(65*"=")
 
data = [] #list kosong yang nanti akan di isi dengan angka-angka random

for i in range(10): #untuk memnentukan berapa banyak angka yang akan berada dalam list
    data.append(randint(1,60)) #untuk menambahkan jangkauan angka yang diinginkan

print('data sebelum di sorting:' , data) #untuk menampilkan data sebelum di sorting
mergesort(data) #untuk memanggil fungsi mergesort di atas, agar dapat mengsorting angka yang berada dalam list
print (f"Merge Sort :  {data} ") #untuk menampilkan hasil sorting menggunakan merge sort


'''
Selanjutnya, ada 2 fungsi yang digunakan untuk mengsorting dengan menggunakan quick sort. 
'''
def quicksort(arr):
    # Jika array kosong atau hanya memiliki satu elemen, return array tersebut
    if len(arr) <= 1:
        return arr
    
    # Pilih pivot dan pisahkan elemen yang lebih kecil dan lebih besar daripada pivot
    pivot = arr[len(arr)//2] #untuk menentukan pivot
    left = [x for x in arr if x < pivot] #apabila elemen lebih kecil dari pivot maka akan dipindahkan ke kiri
    middle = [x for x in arr if x == pivot] #nilai tengah = pivot
    right = [x for x in arr if x > pivot] #apabila elemen lebih besar dari pivot maka akan dipindahkan ke kanan
    
    # Rekursif panggil quicksort pada elemen yang lebih kecil dan lebih besar
    return quicksort(left) + middle + quicksort(right)


arr = [] #list kosong yang nanti akan di isi dengan angka-angka random

for i in range(10):  #untuk memnentukan berapa banyak angka yang akan berada dalam list
    arr.append(randint(10,80)) #untuk menambahkan jangkauan angka yang diinginkan

print(65*"=")
print('data sebelum disorting :',arr) #untuk menampilkan data sebelum di sorting
hasil = quicksort(arr) 
print('Quick Sort :',hasil)  #untuk menampilkan hasil sorting menggunakan quick sort

def shell(list):
    n = len (list) 
    gap = n // 2 #banyak elemen nanti akan dibagi dua yang akan menjadi gap atau rentang dalam mensortingan

#proses sorting
    while gap > 0:
        for i in range (gap, n):
            temp = list[i]
            j=i
            while j >= gap and list [j-gap] > temp:
                list[j] = list[j-gap]
                j -= gap

            list [j] = temp
        gap //= 2

    return list

print(65*"=")

angka = [] #list kosong yang nanti akan di isi dengan angka-angka random

for i in range(10):  #untuk memnentukan berapa banyak angka yang akan berada dalam list
    angka.append(randint(5,70)) #untuk menambahkan jangkauan angka yang diinginkan

print("data sebelum di sorting: ", angka) #untuk menampilkan data sebelum di sorting
print ("Shell Sort : ", shell(angka)) #untuk menampilkan hasil sorting menggunakan quick sort
print(65*"=")