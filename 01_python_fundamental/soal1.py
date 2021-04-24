def convertInput(str):
  output = kalimat.upper().replace(" ", "")
  return ("*" + output + "*")

while True:
  kalimat = input("Masukkan Sebuah Kalimat : ")
  length = len(kalimat)

  if length > 200:
    print("Batas Karakter Maksimal Hanya 200")
  elif length == 0:
    print("Masukkan Sebuah Inputan")
  else:
    print(convertInput(kalimat))
    break
