print("AHWAJ KAFABI")
print("SPK Menghitung metode SAW menggunakan python")
alternatif = ["Produk A", "Produk B", "Produk C", "Produk D"]
kriteria = ["Harga", "Kualitas", "Fitur", "Garansi"]
costbenefit = ["cost", "benefit", "benefit", "benefit"]
kepentingan = [0.3, 0.35, 0.2, 0.15]
alternatifkriteria = [[5000, 70, 10, 36],[6000, 90, 10, 48],[7000, 80, 9, 48],[8000, 70, 8, 60]]
print (str(alternatif))
print (str(kriteria))
print(str(costbenefit))
print(str(kepentingan))
print(str(alternatifkriteria))

pembagi = []
for i in range(len(kriteria)):
     pembagi.append(0)
     for j in range(len(alternatif)):
             if costbenefit[i] == 'cost':
                     if j == 0:
                             pembagi[i] = alternatifkriteria[j][i]
                     else:
                             if pembagi[i] > alternatifkriteria[j][i]:
                                     pembagi[i] = alternatifkriteria[j][i]
             else:   #if costbenefit[i] == 'benefit:
                     if j == 0:
                             pembagi[i] = alternatifkriteria[j][i]
                     else:
                             if pembagi[i] < alternatifkriteria[j][i]:
                                     pembagi[i] = alternatifkriteria[j][i]
print(str(pembagi))

normalisasi = []
for i in range(len(alternatif)):
     normalisasi.append([])
     for j in range(len(kriteria)):
             normalisasi[i].append(0)
             if costbenefit[j] == 'cost':
                     normalisasi[i][j] = pembagi[j] / alternatifkriteria[i][j]
             else:           #if costbenefit[j] == 'benefit':
                     normalisasi[i][j] = alternatifkriteria[i][j] / pembagi[j]
print(str(normalisasi))

hasil = []
for i in range(len(alternatif)):
     hasil.append(0)
     for j in range(len(kriteria)):
             hasil[i] = hasil[i] + (normalisasi[i][j] * kepentingan[j])
print(str(alternatif))
print(str(hasil))

alternatifrangking = []
hasilrangking = []
for i in range(len(alternatif)):
     hasilrangking.append(hasil[i])
     alternatifrangking.append(alternatif[i])

for i in range(len(alternatif)):
     for j in range(len(alternatif)):
             if j > i:
                     if hasilrangking[j] > hasilrangking[i]:
                             tmphasil = hasilrangking[i]
                             tmpalternatif = alternatifrangking[i]
                             hasilrangking[i] = hasilrangking[j]
                             hasilrangking[j] = tmphasil
                             alternatifrangking[j] = tmpalternatif
print(str(alternatifrangking))
print(str(hasilrangking))
