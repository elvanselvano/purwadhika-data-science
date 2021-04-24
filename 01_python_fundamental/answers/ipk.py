
def beasiswa(kode_prodi, ipk):
  # Determine whether a student get beasiswa
  if kode_prodi == "TI" or kode_prodi == "SI":
    if 75 < ipk < 85:
      return 20
    elif 85 < ipk < 100:
      return 30
  elif kode_prodi == "DKV" or kode_prodi == "Teknik Industri":
    if 75 < ipk < 85:
      return 25
    elif 85 < ipk < 100:
      return 35
  
  return 0
  
total_mahasiswa = int(input("Jumlah Mahasiswa: "))
results = []
count_beasiswa = 0

for i in range(total_mahasiswa):
  NIM = input("NIM: ")
  nama = input("Nama: ")
  alamat = input("Alamat: ")
  asal_sekolah = input("Asal Sekolah: ")
  kode_prodi = input("Kode Prodi: ")
  ipk_awal = int(input("IPK awal: "))
  uts = int(input("UTS: "))
  uas = int(input("UAS: "))
  tm = int(input("TM: "))

  # Find IPS and IPK
  ips = 0.3 * uts + 0.3 * tm + 0.4 * uas
  hasil = beasiswa(kode_prodi, (ipk_awal+ips)/2)
  
  # Print student's information
  if hasil > 0:
    results.append(nama + " mendapatkan beasiswa " + str(hasil) + "%.")
    count_beasiswa += 1
  else:
    results.append(nama + " tidak berhasil mendapatkan beasiswa.")

# Print results of beasiswa
for r in results:
  print(r)

# Count number of students who get beasiswa
print("Dari " + str(total_mahasiswa) + " mahasiswa, " + str(count_beasiswa) + " mahasiswa berhasil mendapatkan beasiswa.")
