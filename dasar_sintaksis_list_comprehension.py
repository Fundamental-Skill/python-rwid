print("\nPerintah del")
daftar_buku = ['Seven Habits', 'How To Influence People', 'First Things First', "Extends"]
del daftar_buku[0]
for i in range(len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del denga list comprehension")
daftar_buku = ['Seven Habits', 'How To Influence People', 'First Things First', "Extends"]
del daftar_buku[0:3] #START:END
for i in range(len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del denga list comprehension")
daftar_buku = ['Seven Habits', 'How To Influence People', 'First Things First', "Extends"]
del daftar_buku[0::2] #START:END:STEP
for i in range(len(daftar_buku)):
    print(daftar_buku[i])

print("\nMembuat List Baru")
daftar_buku = ['Seven Habits', 'How To Influence People', 'First Things First', "Extends"]
daftar_buku_baru = daftar_buku[:]
for i in range(len(daftar_buku)):
    print(daftar_buku[i])

print("\nMembuat List Baru")
del daftar_buku[:]
for i in range(len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nMembuat List Baru dengan comprehension: ganjil")
daftar_buku = ['1 Seven Habits', '2 How To Influence People', '3 First Things First', "4 Extends"]
daftar_buku_baru = daftar_buku[::2]
for i in range(len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nMembuat List Baru dengan comprehension: genap")
daftar_buku = ['1 Seven Habits', '2 How To Influence People', '3 First Things First', "4 Extends"]
daftar_buku_baru = daftar_buku[1::2] #start stop end
for i in range(len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nMembuat List Baru dengan comprehension: buang di ujung")
daftar_buku = ['1 Seven Habits', '2 How To Influence People', '3 First Things First', "4 Extends"]
daftar_buku_baru = daftar_buku[0::-1] #start stop end
for i in range(len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nMembuat List Baru dengan comprehension: langsung")
daftar_buku = ['1 Seven Habits', '2 How To Influence People', '3 First Things First', "4 Extends"]
print(daftar_buku[0::2])
