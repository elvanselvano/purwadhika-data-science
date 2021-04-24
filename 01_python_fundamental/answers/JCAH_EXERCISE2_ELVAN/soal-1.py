N = int(input("Masukan Jumlah Baris Maksimal : "))

for i in range(1, N+1):
  for j in range(1, i+1):
    print(str(j) + "  ", end="")
  print()