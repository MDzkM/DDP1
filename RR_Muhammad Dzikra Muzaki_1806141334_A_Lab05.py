file = open("lab5.txt", "r")                    # Membuka file

def decode_file():
    '''Fungsi untuk menerjemahkan sandi.'''
    number_of_sentences = int(file.readline())  # Menentukan banyak kalimat
    pos_list = []                               # Membuat list untuk posisi
    for sentence in range(number_of_sentences): # Membaca kalimat sebanyak n
        current_sentence = file.readline()      # Membaca kalimat per baris
        char_pos = count(current_sentence)      # Memanggil fungsi count
        pos_list.append(char_pos)               # Memasukkan value ke list
    find_code(pos_list)                         # Memanggil fungsi find_code

def count(current_sentence):
    '''Fungsi untuk menentukan posisi tiap karakter terjemahan sandi.'''
    pos = 0                                     # Declare variabel utk posisi
    for char in current_sentence:               # Mengecek tiap karakter
        if char.isdecimal():                    # Mengecek apakah desimal
            pos += int(char)                    # Menjumlah angka pd kalimat
    return pos                                  # Mengembalikan posisi kode

def find_code(pos_list):
    '''Fungsi untuk mencari karakter pada sandi.'''
    code = file.readline()                      # Membaca string kode
    decoded_str = ""                            # Declare string kosong
    for char_code in pos_list:                  # Mencari char untuk tiap kode
        if char_code == 0:                      # Tidak mencetak apabila 0
            continue                            # Skip ke iterasi berikutnya
        else:
            decoded_str += code[char_code - 1]  # Menambahkan char pada string

    # Menulis hasil terjemahan
    print("Pesan rahasia dari Dek Depy adalah: {}".format(decoded_str))

def main():
    decode_file()                               # Memanggil fungsi penerjemah
    file.close()                                # Menutup file

if __name__ == "__main__":                      # Eksekusi fungsi main
    main()
