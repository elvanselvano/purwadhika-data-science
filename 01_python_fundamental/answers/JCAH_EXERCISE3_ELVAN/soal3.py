def sort_odd_even(numbers):
  odd, even = [], [] # initialize empty list

  # for all numbers: if number is even, add to 'even' list, otherwise add to 'odd' list
  for n in numbers:
    even.append(n) if n % 2 == 0 else odd.append(n)
    
  odd.sort() # sort all odd numbers (ascending) [1, 1, 1, 3, 5, 15, 21]
  even.sort(reverse=True) # sort all even numbers (descending) [124, 32, 24, 12, 12, 2, 2]
  print(odd + even) # merge 'odd' and 'even' [1, 1, 1, 3, 5, 15, 21, 124, 32, 24, 12, 12, 2, 2]

sort_odd_even([1,3,2,2,1,5,1,24,12,124,12,21,32,15])