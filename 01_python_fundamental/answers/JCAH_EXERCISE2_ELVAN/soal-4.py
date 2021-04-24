N = input("Input Angka Yang Hendak Dibalik : ")
print("Angka Asli : " + N)

N_reversed = ''
length = len(N)-1

for i in range(length, -1, -1):
  N_reversed += N[i]

print("Angka Setelah Dibalik : " + N_reversed)