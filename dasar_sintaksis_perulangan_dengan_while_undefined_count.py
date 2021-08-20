"""
Program perulangan membaca buku dengan while sampai paham
"""

book_count = 10
print("Perintah Ibu membaca buku")
understood_count = 0
print(f"Jumlah buku yang sudah dibaca dan dipahami {understood_count}\n")
read_count = 0

while read_count < book_count * 2:
    read_count += 1
    if understood_count == 9:
        print(f"Buku ke - {understood_count + 1} belum paham")
    else:
        understood_count += 1
        print(f"Buku ke - {understood_count} sudah dibaca dan dipaham")

print(f"\nJumlah buku yang sudah dibaca dan dipahami {understood_count}")
if understood_count == book_count:
    print("Bu, Semua buku sudah dipahami")
else:
    print(f"Bu, tidak semua buku bisa dipahami, Budi hanya bisa memahami {understood_count} buku")

