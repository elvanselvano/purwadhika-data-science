def sort_odd_even(numbers):
  odd = []
  even = []

  for n in numbers:
    if n % 2 == 0:
      even.append(n)
    else:
      odd.append(n)
    
  odd.sort()
  even.sort(reverse=True)
  print(odd+even)

sort_odd_even([1,3,2,2,1,5,1,24,12,124,12,21,32,15])