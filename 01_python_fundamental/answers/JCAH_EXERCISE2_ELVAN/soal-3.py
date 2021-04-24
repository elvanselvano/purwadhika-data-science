N = int(input("Masukkan Angka : "))
faktorial = 1

if N < 0:
  print("Faktorial Hanya Diperbolehkan Untuk Bilangan Positif")
elif N == 0:
  print("Nilai dari 0! adalah 1")
else:
  for i in range(1, N+1):
    faktorial *= i
  print("Nilai Faktorial Dari " + str(N) + " Adalah " + str(faktorial))