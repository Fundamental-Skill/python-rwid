"""
Program perulangan membaca buku dengan for
"""

jumlah_buku = 10
print("Perintah Ibu membaca buku")
jumlah_buku_dibaca = 0
print(f"Jumlah buku yang sudah dibaca {jumlah_buku_dibaca}")

for hitung in range(0, jumlah_buku):
    print(f"Buku ke - {jumlah_buku_dibaca + 1} sudah dibaca")
    jumlah_buku_dibaca += 1

print(f"Jumlah buku yang sudah dibaca {jumlah_buku_dibaca}")