import os, time
os.system("clear")

print ("          Welcome to Kasirku          ")
print ("======================================")
kasir = input("Masukan nama kasir : ")
tggl = input("Tanggal pembelian : ")
print ("======================================")
os.system("clear")
def menu():
	os.system("clear")
	time.sleep(1)
	print ("============== Welcome ===========")
	print (kasir)
	print (tggl)
	print ("==================================")
	time.sleep(0.5)
	print ("============== MENU ==============")
	print ("[1] Tea                Rp.3000")
	print ("[2] Americano coffe    Rp.5000")
	print ("[3] Cappucino          Rp.6000")
	print ("[4] MilkShake         Rp.10.000")
	print ("[5] Mineral Water      Rp.3000")
	print ("==================================")
	time.sleep(1)
	h = []
	a = 1
	pesan =int(input("Masukan pesanan (nomer menu) : "))
	if pesan == 1:
		harga = 3000
	elif pesan == 2:
		harga = 5000
	elif pesan == 3:
                harga = 6000
	elif pesan == 4:
                harga = 10000
	elif pesan == 5:
                harga = 3000
	else:
		print("Kode pesanan tidak valid, masukan kembali kodenya")
		time.sleep(2)
		while(True):
			menu()
	jumlah =int(input("Masukan jumlah pembelian : "))
	for i in range (jumlah):
		h.append(harga)
	while True:
		nmbh = input("apakah ingin menambahkan/mengurangi pesanan? (tambah/kurang/tidak) : ")
		if nmbh == "tambah":
			tambah = int(input("Masukan Pesanan (Nomor menu) : "))
			if tambah == 1:
				harga = 3000
			elif tambah == 2:
				harga = 5000
			elif tambah == 3:
				harga = 6000
			elif tambah == 4:
				harga = 10000
			elif tambah == 5:
				harga = 3000
			qty = int(input("Masukan jumlah yang akan ditambahkan : "))
			for i in range (qty):
				h.append(harga)
			c = jumlah + qty
			time.sleep(0.5)
			print("")
			print ("Total Pemesanan : ", c)
			bayar=sum(h)
			print ("Total Pembayaran : Rp.{}".format(bayar))
			break
		elif nmbh == "kurang":
			kurang = int(input("Berapa jumlah yang dikurangi : "))
			for x in range (kurang):
				if kurang <= 1:
					a -= kurang
					del h[a]
					bayar = sum(h)
				else:
					kurang -= a
					del h[kurang]
					if kurangi < 0:
						break
			c = jumlah - kurang
			time.sleep(0.5)
			print("")
			print ("Total Pemesanan : ", c)
			bayar = sum(h)
			print ("Total Pembayaran : Rp.{}".format(bayar))
			break
		else:
			bayar =sum(h)
			c =jumlah
			time.sleep(0.5)
			print("")
			print ("Total pemesanan : ", c)
			bayar = sum(h)
			print ("Total Pembayaran : Rp.{}".format(bayar))
			break

	time.sleep(1)
menu()

