import random

N = int(input("Masukkan Jumlah Angka Maksimal : "))
M = int(input("Masukkan Jumlah Angka Pembagi : "))
arr = random.sample(range(1, N), 10)
print(arr)

for number in arr:
  if number % M == 0:
    print(number)