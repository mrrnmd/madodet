print("=====program untuk mengecek bonus dan diskon=====")

total_belanja = int(input("Total Belanja: Rp "))

# jumlah yang harus dibayar adalah berapa total belanjaannya
# tapi kalau dapat diskon akan berkurang
bayar = total_belanja

# jika dia belanja di atas 100rb maka berikan bonus dan diskon
if total_belanja > 100000:
    print("Kamu Mendapatkan Bonus Minuman Dingin")
    print("Dan Diskon 5%")

    # hitung diskonnya
    diskon = total_belanja * 5/100 #5%
    bayar = total_belanja - diskon


# cetak struk
print("Total Yang Harus Dibayar: Rp %s" % bayar)
print("Terima Kasih Sudah Berbelanja")
print("Datang Lagi Yaa...")