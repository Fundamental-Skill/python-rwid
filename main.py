"""
Semua sintaks dasar bahasa pemrograman terdiri dari :
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali" sampai kondisi terpenuhi
"""

# Sekuensial
# print("Ibu berkata, Pergi ke Toko")
# print("Budi menjawab, Baik, apa yang harus saya lakukan di toko")
# print("Ibu menjawab, Beli satu botol susu dan jika ada telor beli 6")
# print("Maka Budi berangkat ke toko")

# Percabangan
jumlah_botol_susu = 173
jumlah_telur = 1678
print(f"Jumlah botol susu: {jumlah_botol_susu} botol")
print(f"Jumlah telur {jumlah_telur} btr")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya dan uangnya cukup")
    print("Budi membeli 1 botol susu")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Menyampaikan hasilnya kepada ibu")
