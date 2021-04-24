def checkPhoneNumber(no):
  if len(no) > 13:
    print("Nomor HP hanya maksimal 13 Angka")
  elif no.startswith("08") == False:
    print("Nomor HP harus dimulai dengan \"08\"")
  else:
    print("Nomor HP Saya Adalah " + no)

nomor = input("Masukkan Nomor HP : ")
checkPhoneNumber(nomor)
