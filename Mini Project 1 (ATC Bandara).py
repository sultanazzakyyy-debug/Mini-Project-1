nama_pesawat = ["Super air jet", "Garuda indonesia", "Citilink"]

arrival = []
departure = []
runway = ""

while True:
    print("\nList ATC Bandara:")
    print("1. Nama-nama pesawat")
    print("2. Menambahkan pesawat")
    print("3. Menghapus pesawat")
    print("4. Tambahkan ke arrival")
    print("5. Tambahkan ke departure")
    print("6. Scheduler")
    print("7. Stop")

    menu = input("Pilih menu menggunakan angka: ")

    #Read
    if menu == "1":
        print("\nDaftar pesawat:\n", nama_pesawat)

    #Create
    elif menu == "2":
        nama = input("\nNama pesawat baru: ")
        nama_pesawat.append(nama)
        print("Pesawat ditambahkan:", nama)

    #Delete 
    elif menu == "3":
        hapus = input("\nNama pesawat yang dihapus: ")
        if hapus in nama_pesawat:
            nama_pesawat.remove(hapus)
            print("Pesawat dihapus:", hapus)
        else:
            print("Pesawat tidak dapat ditemukan")

    #Arrival
    elif menu == "4":
        nama = input("\nNama pesawat yang dimasukkan ke Arrival: ")
        if nama in nama_pesawat:
            arrival.append(nama)
            print("Ditambah ke Arrival:", nama)
        else:
            print("Pesawat tidak terdaftar")

    #Departure
    elif menu == "5":
            nama = input("\nNama pesawat yang dimasukkan ke Departure: ")
            if nama in nama_pesawat:
                departure.append(nama)
                print("Ditambah ke Departure:", nama)
            else:
                print("Pesawat tidak terdaftar")

    #Scheduler
    elif menu == "6":
        print("\n~~~~~Scheduler ATC~~~~~")
        if runway != "":
            print("\nRunway sedang digunakan oleh pesawat:", runway)
            print("Runway sekarang dikosongkan...")
            runway = ""
        elif arrival:
            runway = arrival.pop()
            print("Pesawat", runway, "mendarat (Arrival)")
        elif departure:
            runway = departure.pop()
            print("Pesawat", runway, "lepas landas (Departure)")
        else:
            print("Gak ada pesawat yang menunggu...")

    elif menu == "7":
        print("Program diberhentikan...")
        break
    else:
        print("Menu salah!")