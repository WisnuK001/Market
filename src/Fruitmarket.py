from tabulate import tabulate

def show(database, title='Daftar Buah Tersedia'):
    # Define header
    header = database[0]
    data   = database[1:]

    # show table
    print(tabulate(data, header, tablefmt="outline"))

def add(database):
    #input buah baru
    name = input('input nama buah: ').capitalize()
    stock = int(input('input stock buah: '))
    price = int(input('input harga harga: '))
    index = len(database) - 1 
    #update database
    database = database.append([
        index, name, stock, price
    ])
    return database

def delete(database):
    #input index
    index = int(input('input indeks buah yanng akan dihapus: '))

    # hapus buah berdasarkan index
    for i, val in enumerate(database[1:]):
        if index == val[0]:
            del database[i+1]
            break
        elif index > len(database) - 1:
            print('Buah yang dicari tidak ada')
            break
    
    # update indeks buah

    for i, val in enumerate(database[1:]):
        if val[0] > i:
            database[i+1] = (val[0]-1, val[1], val[2], val[3])
            break
        
    return database

def buy(database):
    Cart = [
        ['nama', 'qty', 'harga'],
    ]