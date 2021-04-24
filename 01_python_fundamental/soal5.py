def longestWord(kalimat):
  words = kalimat.split()
  wordsSorted = sorted(words, key=len)
  maximumLength = len(wordsSorted[-1])
  print("Jumlah Karakter Terbanyak Adalah Sebesar " + str(maximumLength) + " Karakter")

  for i in range(len(wordsSorted)-1, -1, -1):
    if len(wordsSorted[i]) == maximumLength:
      print("Karakter Yang Berjumlah " + str(maximumLength) + " Adalah " + wordsSorted[i])
    else:
      break

kalimat = input("Masukkan Kalimat : ")
longestWord(kalimat)
