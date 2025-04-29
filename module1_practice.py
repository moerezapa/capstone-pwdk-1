menuList = [
    '1. Menampilkan Data Karyawan',
    '2. Menambah Data Karyawan',
    '3. Mengubah Data Karyawan',
    '4. Menghapus Data Karyawan',
    '5. Keluar Aplikasi'
]

dataKaryawan = [
    {
        'NIP': '532335',
        'NamaKaryawan' : 'Cole Palmer',
        'Asal': 'Surabaya'
    },
    {
        'NIP': '532336',
        'NamaKaryawan' : 'Ernando Ari',
        'Asal': 'Semarang'
    },
    {
        'NIP': '532337',
        'NamaKaryawan' : 'Marselino',
        'Asal': 'Lumajang'
    }
]

def readAllData(listKaryawan):
    for karyawan in listKaryawan:
        print(f"{karyawan['NamaKaryawan']} yang berasal dari {karyawan['Asal']} memiliki NIP {karyawan['NIP']}")

def menu1():
    print("======= MENU MELIHAT DATA KARYAWAN =======")
    print("1. Menu Melihat Semua Data Karyawan")
    print("2. Menu Melihat Data Karyawan Tertentu")
    print("3. Kembali")
    subMenu = input("Masukkan menu yang dituju [1-3]: ")
    if subMenu == '1':
        readAllData(listKaryawan= dataKaryawan)
    elif subMenu == '2':
        print("Menggunakan indexing")
    elif subMenu == '3':
        # quit # kembali ke menu sebelumnya
        mainMenu() # kembali ke menu sebelumnya
    else:
        print("Input Anda tidak sesuai!")

def mainMenu():
    userInput = 5

    while userInput != '5':
        for menu in menuList:
            print(menu)

        userInput = input("Masukkan menu yang dituju [1-5]: ")
        if userInput == '1':
            menu1()
        elif userInput == '2':
            print("======= MENU TAMBAH DATA KARYAWAN =======")
        elif userInput == '3':
            print("======= MENU UBAH DATA KARYAWAN  =======")
        elif userInput == '4':
            print("======= MENU HAPUS DATA KARYAWAN =======")
        elif userInput == '5':
            print("Anda telah keluar dari aplikasi.")
        else:
            print("Menu yang Anda pilih tidak sesuai!\n")


mainMenu()