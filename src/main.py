# Init harga dan stock
priceApel = 10000
priceJeruk = 15000
priceAnggur = 20000

stockApel   = 10
stockJeruk  = 7
stockAnggur = 6


# Deklarasi 

def input_fruit(name, stock, price):
    """_summary_

    Args:
        name (_type_): _description_
        stock (_type_): _description_
        rice (_type_): _description_

    Returns:
        _type_: _description_
    """
    while True:
        n= int(input(f"input jumlah {name.capitalize()}: "))
        if n <= stock:
            price = n * price
            break
        else:
            print(f'jumlah terlalu banyak. {name.capitalize()} sisa {stock}')
    return price, n

# # Input jumlah buah cara Day3

# while True:
#     nApel = int(input(' input jumlah apel: '))
#     if nApel <= stockApel:
#         break
#     else:
#         print(f'jumlah terlalu banyak , stok tersisa : {stockApel}')
#         continue

# while True:
#     nJeruk = int(input(' input jumlah jeruk: '))
#     if nJeruk <= stockJeruk:
#         break
#     else:
#         print(f'jumlah terlalu banyak , stok tersisa : {stockJeruk}')
#         continue

# while True:
#     nAnggur = int(input(' input jumlah anggur: '))
#     if nAnggur <= stockAnggur:
#         break
#     else:
#         print(f'jumlah terlalu banyak , stok tersisa : {stockAnggur}')
#         continue



#hitung harga per buah
# totalpriceApel = nApel * priceApel
# totalpriceJeruk = nJeruk * priceJeruk
# totalpriceAnggur = nAnggur * priceAnggur

totalpriceApel, nApel = input_fruit('apel', stockApel, priceApel)
totalpriceJeruk, nJeruk = input_fruit('jeruk', stockJeruk, priceJeruk)
totalpriceAnggur, nAnggur = input_fruit('anggur', stockAnggur, priceAnggur)

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


# Proses Bayar

while True:
    pay = int(input('masukkan jumlah uang anda: '))
    delta = pay - priceTotal
    if delta >= 0:
        print(f'Terima kasih, uang kembalian anda sebesar: {delta}')
        break
    else:
        print(f'uang anda kurang:{abs(delta)}')
