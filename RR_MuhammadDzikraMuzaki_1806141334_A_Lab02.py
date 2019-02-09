# Penginputan banyaknya stempel yang dimiliki
stmp_A = int(input("Banyaknya Stempel A: "))
stmp_B = int(input("Banyaknya Stempel B: "))
stmp_C = int(input("Banyaknya Stempel C: "))
stmp_D = int(input("Banyaknya Stempel D: "))
stmp_Jp = int(input("Banyaknya Stempel Jackpot: "))

# Konversi dari jumlah stempel ke poin
poin_Tot = ((stmp_A * 41) + (stmp_B * 727) + (stmp_C * 104)
+ (stmp_D * 2017) + (2 ** stmp_Jp))

# Assignment nilai poin tiap boneka
Kaka = 2018
Atung = 890
Binbin = 120

# Mencari banyaknya boneka maksimal yang bisa didapat
# Dengan prioritas Kaka, Atung, Binbin
jml_Kaka = int(poin_Tot / Kaka)
poin_Tot = poin_Tot % Kaka

jml_Atung = int(poin_Tot / Atung)
poin_Tot = poin_Tot % Atung

jml_Binbin = int(poin_Tot / Binbin)
poin_Tot = poin_Tot % Binbin

# Mengeluarkan output hasil pencarian banyaknya tiap boneka
print("Rey harus menukarkan ", jml_Kaka, " boneka Kaka, ",
jml_Atung, " boneka Atung, dan ", jml_Binbin,
" boneka Binbin\nPoint sisa sebanyak: ", poin_Tot, " poin\n")
