"""
Program perulangan membaca buku dengan while sampai paham
"""

jumlah_buku = 10
print("Perintah Ibu membaca buku")
jumlah_buku_dibaca_dan_dipahami = 0
print(f"Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_dibaca_dan_dipahami}\n")
total_jumlah_baca = 0

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca += 1
    if jumlah_buku_dibaca_dan_dipahami == 9:
        print(f"Buku ke - {jumlah_buku_dibaca_dan_dipahami + 1} belum paham")
    else:
        jumlah_buku_dibaca_dan_dipahami += 1
        print(f"Buku ke - {jumlah_buku_dibaca_dan_dipahami} sudah dibaca dan dipaham")

print(f"\nJumlah buku yang sudah dibaca dan dipahami {jumlah_buku_dibaca_dan_dipahami}")
if jumlah_buku_dibaca_dan_dipahami == jumlah_buku:
    print("Bu, Semua buku sudah dipahami")
else:
    print(f"Bu, tidak semua buku bisa dipahami, Budi hanya bisa memahami {jumlah_buku_dibaca_dan_dipahami} buku")

