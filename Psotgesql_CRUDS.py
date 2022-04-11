import psycopg2 as db
import os

con = None
connected = None
cursor = None

def connect():
    global connected
    global con
    global cursor
    try:
        con = db.connect( 
            host = "localhost", 
            database = "kampus", 
            port = 5432, 
            user = "tegara", 
            password = "tegar1234"
        )
        cursor = con.cursor()
        connected = True
    except:
        connected = False
    return cursor #ini di ubah sesuai dengan database yang dimiliki

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
    print("PostgreSQL : Disconnected")

def create_data():
    try:
        nim = input("Masukan NIM            : ")
        nama = input("Masukan Nama Lengkap   : ")
        idprodi = input("Masukan ID Prodi       : ")
        a = connect()
        sql = "insert into mahasiswa (nim, nama, idprodi) values ('"+nim+"', '"+nama+"', '"+idprodi+"')"
        a.execute(sql)
        con.commit()
        print ("Complete. \n")
    except(Exception, db.Error) as error:
        print ("Warning, terjadi kesalahan", error)

    finally:
        disconnect()

def read_data():
    try:
        a = connect()
        sql = "select * from mahasiswa"
        a.execute(sql)
        record = a.fetchall()
        
        for row in record:
            print("nim          = ", row[1])
            print("nama         = ", row[2])
            print("idprodi      = ", row[3])
            print("idfakultas   = ", row[4],"\n")
        return record

    except(Exception, db.Error) as error:
        print ("Warning, terjadi kesalahan", error)

    finally:
        disconnect()

def update_data():
    try:
        nim = input("Masukan NIM : ")
        a = connect()
        sql = "select * from mahasiswa where nim = '"+nim+"'"
        a.execute(sql)
        record = a.fetchall()
        print ("Data saat ini : ")
        
        for row in record:
            print("nim          = ", row[1])
            print("nama         = ", row[2])
            print("idprodi      = ", row[3], "\n")
        
        row = a.rowcount

        if(row==1):
            print ("Silahkan input untuk mengubah data...")
            nama = input("Masukan Nama Lengkap  : ")
            idprodi = input("Masukan ID Prodi     : ")
            a = connect()
            sql = "update mahasiswa set nama='"+nama+"', Idprodi='"+idprodi+"' where nim='"+nim+"'"
            a.execute(sql)#ini juga
            con.commit()
            print ("Complete. \n")
            
            sql = "select * from mahasiswa where nim = '"+nim+"'"
            a.execute(sql)
            rec = a.fetchall()
            print ("Done : ")
            
            for row in rec:
                print("nim          = ", row[1])
                print("nama         = ", row[2])
                print("Idprodi      = ", row[3], "\n")
            
            return record
            
        else:
            print ("Data tidak ditemukan. \n")

    except(Exception, db.Error) as error:
        print ("Warning, terjadi kesalahan ", error)

    finally:
        disconnect()
    
def delete_data():
    try:
        nim = input("Masukan NIM : ")
        a = connect()
        sql = "select * from mahasiswa where nim = '"+nim+"'"
        a.execute(sql)
        record = a.fetchall()
        print ("Data saat ini : ")
        
        for row in record:
            print("nim          = ", row[1])
            print("nama         = ", row[2])
            print("Idprodi      = ", row[3], "\n")
    
        row = a.rowcount

        if(row==1):
            jwb = input("Apakah anda ingin menghapus data ini? (y/t)")
            if(jwb.upper()=="Y"):
                a = connect()
                sql = "delete from mahasiswa where nim='"+nim+"'"
                a.execute(sql)
                con.commit()
                print ("Delete Complete. \n")
            else:
                print ("Cancel Delete . \n")
        else:
            print ("Not Found. \n")

    except(Exception, db.Error) as error:
        print("Warning , Terjadi Kesalahan ", error)

    finally:
        disconnect()
    
def search_data():
    try:
        nim = input("Masukan NIM : ")
        a = connect()
        sql = "select * from mahasiswa where nim = '"+nim+"'"
        a.execute(sql)
        record = a.fetchall()
        for row in record:
            print("nim          = ", row[1])
            print("nama         = ", row[2])
            print("Idprodi      = ", row[3])
            print("idfakultas   = ", row[4] ,"\n")
    
        print ("Search Complete. \n")
        return record

    except(Exception, db.Error) as error:
        print("Warning, terjadi kesalahan ", error)

    finally:
        disconnect()

print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print ( " Nama : Muhammad Tegar Abubakar" )
print ( " Nim  : 200511047" )
print ( " Kelas: R1" )
print ("----------------------------")
def show_menu():
    print("\n=== Python Database Apk ===")
    print("1. Insert Data")
    print("2. Show Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Search Data")
    print("0. Close")
    print("------------------")
    menu = input("Pilih menu> ")

 
    os.system("cls")

    if menu == "1":
        create_data()
    elif menu == "2":
        read_data()
    elif menu == "3":
        update_data()
    elif menu == "4":
        delete_data()
    elif menu == "5":
        search_data()
    elif menu == "0":
        print ( "---------------------" )
        print ( " program finish, your program success" )
        print ( "--------------------- \n" )
        exit()
    else:
        print("Wrong Menu!")

if __name__ == "__main__":
  while(True):
    show_menu() 