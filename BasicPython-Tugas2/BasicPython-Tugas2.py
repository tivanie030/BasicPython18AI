Nama = ['Tiffany', 'Devon']
NoTelepon = ['08123456789', '08987654321']


def DaftarKontak():  # fungsi untuk menampilkan kontak yang tersimpan di list kontak
    print('Daftar Kontak:')
    for i in range(len(Nama)):
        print('Nama: {}'.format(Nama[i]))
        print('No Telepon: {}'.format(NoTelepon[i]))


def TambahKontak():  # fungsi untuk menambahkan kontak
    Nama.append(input('Nama: '))
    NoTelepon.append(input('No Telepon: '))
    print('Kontak berhasil ditambahkan')


print('Selamat datang!')
while True:
    print('---Menu---')
    print('1. Daftar Kontak')
    print('2. Tambah Kontak')
    print('3. Keluar')
    menu = int(input('Pilih Menu: '))
    if menu == 1:
        DaftarKontak()
    elif menu == 2:
        TambahKontak()
    elif menu == 3:
        print('Program selesai, sampai jumpa!')
        break
    else:
        print('Menu tidak tersedia')
