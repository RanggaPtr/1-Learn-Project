# operator perbandingan
# >, <, >=, <=, ==, !=
a=10
b=5
c=10

# <
print(a,"<",b,"=",a<b)

# >
print(a,">",b,"=",a>b)

# <=
print(a,"<=",b,"=",a<=b)

# >=
print(a,">=",b,"=",a>=b)

# ==
print(a,"==",b,"=",a==b)

# !=
print(a,"!=",b,"=",a!=b)

# is sebagai komparasi object identity
x=9
y=9
print("Membandingkan bilangan biasa")
print(x,"is",y,"=",x is y) # ini berlaku jika bilangan biasa
print(x,"==",y,"=",x == y)

# jika data berupa list makan akan muncul hasilnya yang berbeda karena hasil yang kira dapatkan berupa menkomper lokasi memory
print("Membandingkan list")
x=[1,2,3] 
y=[1,2,3]
print("nilai x=",x,"id x=",hex(id(x)))
print("nilai y=",y,"id y=",hex(id(y)))
print(x,"==",y,"=",x == y)#ini akan membandingkan value nya yang otomatis akan true
print(x,"is",y,"=",x is y)  #ini akan membandingkan lokasinya yang otomatis akan false 

x=9
y=9
print("nilai x=",x,"id x=",hex(id(x)))
print("nilai y=",y,"id y=",hex(id(y)))
# hex id untuk mengetahui id memory

# is not
print(x,"is not",y,"=",x is not y)

# in
list=[1,2,3,4,5]
print(1 in list)
print(6 in list)

# not in
print(1 not in list)
print(6 not in list)





