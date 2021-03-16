def makeShape(n):
  print(' ' * (n-1) + '***' + ' ' * (n-1))

  for i in range(1, n-1):
    spasi = n-i-1
    spasiTengah = i*2-1
    print(spasi * ' ' + "**" + spasiTengah * ' ' + "**" + spasi * ' ' )

  print("*" * (2*n+1))

n = int(input("Masukkan Jumlah Baris : "))
makeShape(n)

