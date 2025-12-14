nilai = []

jumlah_input = int(input("Berapa banyak nilai yang ingin dimasukkan? "))

for i in range(jumlah_input):
    data = input(f"Masukkan nilai ke-{i+1}: ")

    try:
        angka = float(data)
        nilai.append(angka)
    except ValueError:
        print("Input bukan angka, data dilewati.")

total = 0
jumlah_data_valid = 0

for n in nilai:
    try:
        total += n
        jumlah_data_valid += 1
    except TypeError:
        continue

if jumlah_data_valid > 0:
    rata_rata = total / jumlah_data_valid
    print("Rata-rata nilai:", rata_rata)
else:
    print("Tidak ada nilai yang valid.")
