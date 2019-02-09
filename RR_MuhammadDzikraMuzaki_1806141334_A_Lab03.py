import string

# string bernilai "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = string.ascii_uppercase

def base_n_to_int(number, base):
    """Fungsi untuk mengubah nilai dari basis n ke desimal."""

    value = 0

    # mengiterasi string dari belakang dengan indeksnya.
    for exponent, digit in enumerate(reversed(number)):

        # nilai digit desimal.
        if digit.isdecimal():
            digit_value = int(digit)

        # nilai digit huruf.
        else:
            digit_value = alphabet.index(digit) + 10

        value += digit_value * base ** exponent

    return value

def int_to_base_n(value, base):
    """Fungsi untuk mengubah desimal menjadi basis n."""

    base_n = ""

    # membagi value hingga 0 dan menyimpan sisanya.
    while value != 0:
        temp = value % base
        value //= base

        # mengubah hasil modulo lebih dari 10 ke alfabet.
        if temp > 10:
            temp = alphabet[temp-10]

        # menyimpan hasil pembagian dalam string.
        base_n += str(temp)

    return base_n

def main():
    """Fungsi utama money changer."""

    # meminta input uang dalam desimal.
    value = int(input("Masukkkan uang yang dimiliki Rey: Rp. "))

    # meminta input basis yang akan dikonversikan.
    base = int(input("Masukkan mata uang yang ingin ditukarkan: "))

    # mengecek nilai base agar memenuhi range
    while not (2 <= base <= 36):
        print("Pastikan Anda memasukkan mata uang yang valid!")
        base = int(input("Masukkan mata uang yang ingin ditukarkan: "))

    # mengubah nilai desimal ke basis n.
    converted_value = int_to_base_n(value, base)
    print("Rey menukarkan Rp. {} menjadi $ {} dan berangkat ke luar negeri".format(value, converted_value))

    # meminta input uang yang akan dibelanjakan.
    number = input("Masukkan uang yang Rey belanjakan di luar negeri: $ ")

    # menghitung sisa uang yang dimiliki.
    total_value = int(value) - base_n_to_int(number, base)
    print("Rey kembali ke kampung halaman dengan sisa uang: Rp. {}".format(total_value))

if __name__ == "__main__":
    # fungsi main akan dipanggil jika program dieksekusi.
    main()
