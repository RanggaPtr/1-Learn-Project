# operasi dan manipulasi string

# menggabungkan string
namaPertama="rangga"
namaTengah=" putra "
namaAkhir="syananda budhi"
print(namaPertama+
namaTengah+namaAkhir)

namaLengkap=namaPertama+namaTengah+namaAkhir
print(namaLengkap)

# menghitung panjang string
panjangString=len(namaLengkap)
print("Panjang dari string ",namaLengkap," :",str(panjangString))

# operator untuk string
# mengecek apakah ada komponen string atau char didalam string

r="r" #CASE SENSYTIVE
status=r in namaLengkap
print("Char"+r+" ada di "+ namaLengkap+" ?",str(status))

# mengulangi string
print("wk"*10)

# indexing
print("index ke-0 :"+namaLengkap[0])
print("index ke-26 :"+namaLengkap[26])
print("indec ke-1 :"+namaLengkap[-1])

