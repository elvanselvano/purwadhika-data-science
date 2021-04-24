start = int(input("Angka Awal : "))
end = int(input("Angka Akhir : "))
primes = []

for i in range(start, end):
  currentNumber = i
  isPrime = True

  if currentNumber == 1:
    isPrime = False

  for j in range(2, i-1):
    if currentNumber % j == 0:
      isPrime = False
      break
  
  if isPrime:
    primes.append(currentNumber)

print("Total Bilangan Prima Diantara " + str(start) + " dan " + str(end) + " Sebanyak " + str(len(primes)) + " Bilangan" )
print("Berikut Ini Daftar Bilangan Prima Dari Rentan Tersebut")

for prime in primes:
  print(prime)

