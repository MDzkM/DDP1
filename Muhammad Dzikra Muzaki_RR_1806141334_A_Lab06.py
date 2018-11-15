def print_sentence(banyak_kelompok, lists_of_set):
    '''Fungsi mencetak kalimat output'''

    # Menset jumlah datang total awal
    jumlah_datang_total = 0

    # Mencetak kalimat kehadiran tiap kelompok
    for nomor_kelompok in range(banyak_kelompok):

        # Menjumlahkan anggota kelompok yang hadir
        jumlah_orang = len(lists_of_set[nomor_kelompok])
        print("Banyak anggota pada Kelompok {} adalah {} orang"
        .format(nomor_kelompok+1, jumlah_orang))

        # Menjumlahkan anggota kelompok yang hadir ke kehadiran total
        jumlah_datang_total += jumlah_orang

    # Mencetak kalimat kehadiran total
    print("Banyak orang yang hadir hari ini adalah {} orang"
    .format(jumlah_datang_total))

def count_kehadiran(file_absensi, banyak_kelompok, lists_of_set):
    ''' Fungsi menghitung banyak anggota yang hadir'''

    # Membaca baris sebanyak kelompok
    for data in range(banyak_kelompok):

        # Membaca baris kelompok
        temp = file_absensi.readline().lower().split()

        # Menentukan kelompok baris
        kelompok = int(temp[0]) - 1

        # Membuat list nama dalam baris
        temp_nama = temp[1:len(temp)]

        # Memasukkan tiap nama dalam baris ke dalam set kelompok itu
        for nama in temp_nama:
            lists_of_set[kelompok].add(nama)

def main():
    # Membuka file absensi
    file_absensi = open("Lab6.txt", "r")

    # Menentukan banyak kelompok
    banyak_kelompok = int(file_absensi.readline())

    # Membuat set sebanyak kelompok
    lists_of_set = [set() for i in range(banyak_kelompok)]

    count_kehadiran(file_absensi, banyak_kelompok, lists_of_set)

    # Membaca baris kosong
    file_absensi.readline()

    count_kehadiran(file_absensi, banyak_kelompok, lists_of_set)

    # Menutup file absensi
    file_absensi.close()

    print_sentence(banyak_kelompok, lists_of_set)

if __name__ == '__main__':
    main()
