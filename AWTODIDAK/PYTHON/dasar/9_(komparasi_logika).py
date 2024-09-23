# latihan logika dan komparasi

# membuat rentang area rentang dari angka
# ++++++++++ 3---------10++++++++++

inputUser=float(input("masukkan angka rentang kurang dari 3  atau lebih  dari 10 :"))

# pemeriksaan inputUSer apakah kurang dari 3
isKurangDari3=inputUser<3
print(isKurangDari3)

# pemeriksaan inputUSer apakah lebih dari 10
isLebihDari10=inputUser>10
print(isLebihDari10)

print("================================================================")
isCorrect=isKurangDari3 or isLebihDari10
print("input rentang kurang dari 3  atau lebih  dari 10 :",isCorrect)


# ---------3+++++++++++10-----------
# pemeriksaan inputUSer apakah rentang tengah
isTengah=(inputUser>=3) and (inputUser<=10)
print("input rentang tengah :",isTengah)

# tugas1
# --------0++++++++++5----------8+++++++++++11--------
isTugas1=(inputUser>=0) and (inputUser<=5) or (inputUser>=8) and (inputUser<=11)
print("input tugas :",isTugas1)

# tugas2
# +++++++0--------5++++++8-------11+++++++
isTugas2=(inputUser<=0) or (inputUser>=5) and (inputUser<=8) or (inputUser>=11)
print("input tugas :",isTugas2)


