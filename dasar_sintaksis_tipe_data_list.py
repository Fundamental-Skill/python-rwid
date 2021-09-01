daftar_buku = ['Seven Habits', 'How To Influence People', 'First Things First']
# print("Tampilkan variable daftar_buku")
# print(daftar_buku)
#
# for buku in daftar_buku:
#     print(buku)
#
# print(daftar_buku[0])

for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# Append untuk menambah List dibelakang
daftar_buku.append("Extends")

print(daftar_buku)

# Clear List
print("\nClear List")
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nGanti elemen pertama")
daftar_buku = ['Seven Habits', 'How To Influence People', 'First Things First', "Extends"]
daftar_buku[0] = "Eigh Habits"
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMengambil elemen ke-2")
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nBuku yang diambil")
print(buku)

print("\n Pop mengambil elemn paling belakang jika tidak di isi indexnya")
daftar_buku.pop()
for i in range(len(daftar_buku)):
    print(daftar_buku[i])

print("\n Pop minus - ")
daftar_buku = ['Seven Habits', 'How To Influence People', 'First Things First', "Extends"]
daftar_buku.pop(-4)
for i in range(len(daftar_buku)):
    print(daftar_buku[i])

print("\nMenambahkan di element depan 'INSERT'")
daftar_buku = ['Seven Habits', 'How To Influence People', 'First Things First', "Extends"]
daftar_buku.insert(0, "OooIII")
for i in range(len(daftar_buku)):
    print(daftar_buku[i])

