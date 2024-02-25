import psycopg2 as db
import os

def connect():
    global connected
    global con
    global cursor

    try :
        con = db.connect(
            host = "localhost",
            port = 5432,
            database = "kampus",
            user = "tegara",
            password = "tegar1234"
        )
        cursor = con.cursor()
        connected = True
    except :
        connected = False
    return cursor

def disconnect():
    global connected
    global con
    global cursor

    if (connected==True):
        cursor.close()
        con.close()
    else:
        con = None
    connected = False

# get all data from db
def Tampil():
    a = connect()
    sql="SELECT * FROM mahasiswa"
    a.execute(sql)
    record = a.fetchall()

    if a.rowcount < 0:
        throwMessage('notfound')
    else:
        for data in record:
            print(data)

def Entry():
   
    n_nim = input("Masukan NIM mahasiswa: ")
    n_nama = input("Masukan nama mahasiswa: ")
    n_idfk = input("Masukan id fakultas mahasiswa: ")
    n_idpr = input("Masukan id prodi mahasiswa: ")

    val = (n_nim,n_nama,n_idfk,n_idpr)
    a = connect()
    sql = "INSERT INTO mahasiswa (nim, nama, idfakultas, idprodi) values (%s,%s,%s,%s)"
    a.execute(sql,val)
    con.commit()

    throwMessage('Done')

def Cari():
    
    os.system("cls")
    Tampil()
    keyword = input("Masukan Nim : ")

    a = connect()
    sql = "SELECT * FROM mahasiswa WHERE nama LIKE %s OR nim LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    a.execute(sql,val)
    record = a.fetchall()

    if a.rowcount < 0:
        throwMessage('Tidak Ditemukan')
    else:
        for data in record:
            print(data)

def Ubah():
    
    os.system("cls")
    Tampil()
    nim = input("Masukkan nim yang akan dirubah: ")

    a = connect()
    sql = "SELECT * FROM mahasiswa WHERE nim='"+ nim +"'"
    a.execute(sql)
    record = a.fetchall()
    print("Data saat ini : {}".format(record))

    if(a.rowcount == 1):
        confirmToUpdate = input("Apakah data ini benar punya anda? (y/n): ")
        if(confirmToUpdate == 'y' or confirmToUpdate == 'Y'):
            print("\n===== MASUKAN PERUBAHAN DATA =====")
            n_nim = input("Masukan NIM mahasiswa: ")
            n_nama = input("Masukan nama mahasiswa: ")
            n_idfk = input("Masukan id fakultas mahasiswa: ")
            n_idpr = input("Masukan id prodi mahasiswa: ")
            val = (n_nim,n_nama,n_idfk,n_idpr, nim)

            a = connect()
            sql = "UPDATE mahasiswa SET nim=%s, nama=%s, idfakultas=%s, idprodi=%s WHERE nim=%s"
            a.execute(sql, val)
            con.commit()
            throwMessage('Done')

            # print the changes
            sql="SELECT * FROM mahasiswa WHERE nim='"+ n_nim +"'"
            a.execute(sql)
            record = a.fetchall()
            print("Data setelah diubah: {}".format(record))
        elif(confirmToUpdate == 'n' or confirmToUpdate == 'N'):
            throwMessage('tidak diubah')
        else:
          throwMessage('')
    else:
        throwMessage('notfound')

def Hapus():
    
    os.system("cls")
    Tampil()
    nim = input("Cari nim yang akan dihapus : ")

    a = connect()
    sql = "SELECT * FROM mahasiswa WHERE nim='"+ nim +"'"
    a.execute(sql)
    record = a.fetchall()
    print("Data saat ini :")
    print(record)

    if(a.rowcount == 1):
        confirmToDelete = input("Apakah Anda yakin akan menghapus mahasiswa tersebut? (y/n): ")
        if(confirmToDelete == 'y' or confirmToDelete == 'Y'):
            sql = "DELETE FROM mahasiswa WHERE nim='"+ nim +"'"
            a.execute(sql)
            con.commit()
            throwMessage('dihapus')
        elif(confirmToDelete == 'n' or confirmToDelete == 'n'):
            throwMessage('tidak terhapus')
        else:
            throwMessage('')
    else:
        throwMessage('tidak ditemukan')

# message
def throwMessage(mess):
    if mess == 'tidak ditemukan':
        print("Data mahasiswa tidak ditemukan!")
    elif mess == 'done':
        print("Data mahasiswa berhasil disimpan!")
    elif mess == 'dihapus':
        print("Data mahasiswa berhasil dihapus!")
    elif mess == 'tidak dihapus':
        print("Data mahasiswa batal untuk dihapus!")
    elif mess == 'diubah':
        print("Data mahasiswa berhasil dirubah!")
    elif mess == 'tidak diubah':
        print("Data mahasiswa batal untuk dirubah!")
    else:
        print("Pesan atau input tidak dikenali!")

def show_menu():
    print("=== APLIKASI DATABASE CRUD PY ===")
    print("1. Tampilkan Data")
    print("2. Insert Data")
    print("3. Cari Data")
    print("4. Update Data")
    print("5. Hapus Data")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu > ")

    os.system("cls")
<!-------main menu-------!>
    if menu == "1":
        Tampil()
    elif menu == "2":
        Entry()
    elif menu == "3":
        Cari()
    elif menu == "4":
        Ubah()
    elif menu == "5":
        Hapus()
    elif menu == "0":
        exit()
    else:
        print("Menu Tidak Ditemukan!")

if __name__ == "__main__":
  while(True):
    show_menu()
