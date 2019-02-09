def convert(angka, target):
    """Mengubah desimal menjadi basis n."""

    # Dictionary untuk nilai di atas 9.
    values = {10 : 'a', 11 : 'b', 12 : 'c', 13 : 'd', 14 : 'e', 15 : 'f'}

    # Base case untuk rekursi.
    if angka == 0:
        return "0"

    result = ""

    # Mencari hasil modulo angka oleh target.
    temp_result = angka % target

    # Mengonversi hasil di atas 9.
    if temp_result > 9:
        temp_result = values[temp_result]

    # Menambahkan hasil modulo dan memanggil rekursi.
    result += convert((angka // target), target) + str(temp_result)

    # Menghapus angka 0 di awal string.
    if result[0] == '0':
        return result[1:]

    # Mengembalikan hasil konversi.
    return result

def main():

    # Meminta input dari user.
    angka = input("Masukkkan angka untuk dikonversi: ")
    target = input("Masukkan base tujuan (2-16): ")

    # Meminta input ulang apabila tidak sesuai.
    while not (2 <= int(target) <= 16):
        print("Pastikan Anda memasukkan base yang valid!")
        target = input("Masukkan base tujuan (2-16): ")

    # Mencetak hasil konversi.
    print("Hasil konversinya: " + convert(int(angka), int(target)))

if __name__ == "__main__":
    main()
