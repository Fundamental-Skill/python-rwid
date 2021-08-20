"""
Program perulangan membaca buku dengan while
"""

jumlah_buku = 10
print("Perintah Ibu membaca buku")
jumlah_buku_dibaca = 0
print(f"Jumlah buku yang sudah dibaca {jumlah_buku_dibaca}\n")

while jumlah_buku_dibaca < jumlah_buku:
    jumlah_buku_dibaca += 1
    print(f"Baca 1 buku yang belum dibaca ke - {jumlah_buku_dibaca}")

print(f"\nJumlah buku yang sudah dibaca {jumlah_buku_dibaca}")
