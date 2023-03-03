import random #sebagai library agar bisa terpanggil
list = [6,2,5,9,4,1,8,3,10,7] #list yang sudah tersedia
random.shuffle(list) #berfungsi untuk mengacak angka di dalam list

def quickShort(list): #algoritma yang digunakan untuk menjalankan function dibawahnya
    if len(list) <= 1: #jika panjang list kurang dari sama dengan 1 maka tampilkan list
        return list
    else:
        pivot = list[0] #pivot untuk mengambil nilai tengah untuk dibandingkan dengan list yg sudah tersedia
        print(f"Pivot : {pivot}")
        less = [x for x in list[1:] if x <= pivot] #variabel l menyimpan nilai x dari list index ke-1 jika x kurang dari pivot akan masuk ke less
        greater = [x for x in list[1:] if x > pivot] #variabel l menyimpan nilai x dari list index ke-1 jika x lebih dari pivot akan masuk ke greater
        return quickShort(less) + [pivot] + quickShort(greater)


def merge_sort(list): #sebagai parameter agar bisa dipanggil
    for post_selanjutnya in range(len(list)-1,0,-1):
        post_max = 0 #untuk menampilkan pivot keberapa
        for x in range(1,post_selanjutnya+1):
            max_sementara = list [post_max] #variabel baru untuk menyimpan list sementara atau yg telah dipecah
            if max_sementara < list[x]: #jika variabel kurang dari list maka tertambah ke variabel baru
                post_max = x
        list [post_max],list [post_selanjutnya] = list [post_selanjutnya],list[post_max]
    

def pilih () : #digunakan untuk user agar bisa memilih ingin menggunakan sort yang mana
    print("|===============|")
    print("| 1. Quick Sort |")
    print("| 2. Merge Sort |")
    print("|===============|")

    n = input("Pilih yang diinginkan : ") #inputan dari user
    if n == "1" : #jika user memilih 1 maka 
        print(quickShort(list)) #jika pilihan 1 yaitu quicksort, maka quicksort akan menjalankan tugasnya dan menampilkan hasilnya
        k = input("Ingin kembali : ") #variabel yang menyimpan inputan kembali dari user 
        if k == "y" : #jika user memilih ya maka akan kembali ke def pilihan
            pilih()
    elif n == "2" : #jika user memilih 2 maka 
        print('Sebelum disort:', list) #jika pilihan 1 yaitu mergesort, maka mergesort akan menjalankan tugasnya dan menampilkan hasilnya
        merge_sort (list)
        print('Sesudah disort:',list)


pilih()