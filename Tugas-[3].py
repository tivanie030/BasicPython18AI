teori = int(input('berapa nilai ujian teorinya? '))
praktek = int(input('berapa nilai ujian prakteknya? '))

if teori and praktek > 70:
    print('Selamat, Anda lulus!')
elif teori > 70 and praktek < 70:
    print('Anda harus mengulang ujian praktek')
elif teori < 70 and praktek > 70:
    print('Anda harus mengulang ujian teori')
else:
    print('Anda harus mengulang ujian teori dan praktek')