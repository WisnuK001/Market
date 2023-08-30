# Init harga
priceApel = 10000
priceJeruk = 15000
priceAnggur = 20000

# Input jumlah buah
nApel = int(input("input jumlah apel : "))
nJeruk = int(input("input jumlah jeruk: "))
nAnggur = int(input("input jumlah anggur: "))

#hitung harga per buah
totalpriceApel = nApel * priceApel
totalpriceJeruk = nJeruk * priceJeruk
totalpriceAnggur = nAnggur * priceAnggur

# Hitung harga total buah
priceTotal = totalpriceAnggur + totalpriceApel + totalpriceJeruk

#show
print( 
    f'''
Detail Belanja

Apel    : {nApel} x {priceApel}
Jeruk   : {nJeruk} x {priceJeruk}
Anggur  : {nAnggur}  x {priceAnggur}
Total   : {priceTotal}

'''
)