import random

def rock_paper_scissors(ronde, name):
    """Fungsi untuk melakukan permainan batu gunting kertas"""
    print(f"===== RONDE {ronde} =====")
    lst_pilihan = ['GUNTING', 'KERTAS', 'BATU']

    poin_user = 0
    poin_rey = 0

    pilihan = input("Masukkan pilihan (GUNTING, KERTAS atau BATU): ")

    # Meminta input user selama belum sesuai.
    while pilihan.upper() not in lst_pilihan:
            pilihan = input("Masukkan pilihan (GUNTING, KERTAS atau BATU): ")
    pilihan_uppercase = pilihan.upper()

    # Menentukan pilihan R.E.Y.
    pilihan_rey = lst_pilihan[random.randint(0, 2)]
    print(f"Rey memilih {pilihan_rey}")

    # Mengecek hasil permainan.
    if (pilihan_uppercase == 'GUNTING') and (pilihan_rey) == 'KERTAS':
        poin_user += 1
        print(f"Ronde dimenangkan oleh {name}!")
    elif (pilihan_uppercase == 'KERTAS') and (pilihan_rey) == 'BATU':
        poin_user += 1
        print(f"Ronde dimenangkan oleh {name}!")
    elif (pilihan_uppercase == 'BATU') and (pilihan_rey) == 'GUNTING':
        poin_user += 1
        print(f"Ronde dimenangkan oleh {name}!")
    elif pilihan_uppercase == pilihan_rey:
        poin_user += 0
        print("Ronde seri!")
    else:
        poin_rey += 1
        print("Ronde dimenangkan oleh Rey!")

    lst_temp = [poin_rey, poin_user]
    
    # Mengembalikan hasil permainan.
    return lst_temp

def main():
    # Output awal permainan.
    print("====================================\
\n== Welcome to Rock Paper Scissors ==\
\n====================================")

    # Meminta input nama.
    print("Hai, aku Rey! Sebelum kita bermain, \
kenalan dulu yuk!")
    name = input("Masukkan nama: ")

    # Meminta input poin maksimal.
    print(f"Halo {name}, senang bertemu denganmu! \
Kamu mau main sampai berapa poin?")
    poin_maks = input("Masukkkan poin maksimal: ")

# Mengecek apakah poin maksimal valid.
    if (poin_maks.isdecimal() == True):
        poin_maks_int = int(poin_maks)
        if poin_maks_int < 1:
            print("Poin maksimal tidak valid! Rey \
mengambek dan meninggalkan permainan karena kamu tidak serius.")
            return

    if (poin_maks.isdecimal() != True):
        print("Poin maksimal tidak valid! Rey \
mengambek dan meninggalkan permainan karena kamu tidak serius.")
        return

    print("====== START ======")
    print(f"Ayo mulai bermain! Tenang saja ya {name}, \
Rey gak bakal ngintip pilihanmu kok.")

    lst_skor = [0, 0]
    ronde = 1

    # Mulai permainan.
    while ronde <= poin_maks_int or lst_skor[0] == lst_skor[1]:
        lst_temp1 = [0, 0]
        lst_temp1 = rock_paper_scissors(ronde, name)
    
        x = lst_temp1[0]
        y = lst_temp1[1]

        lst_skor[0] += x
        lst_skor[1] += y

        print(f"Hasil Sementara: Rey {lst_skor[0]} - {lst_skor[1]} {name}")
        ronde += 1

    if lst_skor[0] > lst_skor[1]:
        print(f"Permainan dimenangkan oleh Rey dengan skor Rey {lst_skor[0]} - \
{lst_skor[1]} {name}!")
    else:
        print(f"Permainan dimenangkan oleh {name} dengan skor Rey {lst_skor[0]} - \
{lst_skor[1]} {name}!")

if __name__ == "__main__":
    main()