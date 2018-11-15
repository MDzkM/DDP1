from fungsi import *


def main():
 
    ## Meminta input dari dua kelompok
    words1 = input("Masukan kata-kata untuk kelompok pertama: ")
    words2 = input("Masukan kata-kata untuk kelompok kedua: ")
 
    ## Mengubah input menjadi list dengan di split ','
    # kemudian dijadikan himpunan
    set1 = set(words1.split(','))
    set2 = set(words2.split(','))

    ## Membuat set yang berisi kata yang terdapat pada set1 dan set2
    intersection_set = set1.intersection(set2)
 
    ## Set Kosong untuk himpunan palindrom dan non palindrom
    palindrom_set = set()
    non_palindrom_set = set()

    ## Looping untuk memisahkan kata palindrom dan tidak
    # kata palindrom dimasukkan ke palindrom_set
    # kata bukan palindrom dimasukkan ke non_palindrom_set
    for word in intersection_set:
        if check_palindrom(word) == True:
            palindrom_set.add(word)
        else:
            non_palindrom_set.add(word)
 
    ## Set baru untuk palindrom baru
    new_palindrom_set = set()
 
    ## Mengubah kata-kata non-palindrom menjadi palindrom
    for s in non_palindrom_set:
        new_palindrom_set.add(make_palindrom(s))
 
 
    ## Mencetak string-string palindrom
    print("Input palindromes: ", end='')
    for s in palindrom_set:
        print(" {}".format(s), end='')
 
    print()
 
    ## Mencetak string-string palindrom baru
    print("New created palindromes: ", end='')
    for s in new_palindrom_set:
        print(" {}".format(s), end='')
 
 
if __name__ == '__main__':
    main()
 
