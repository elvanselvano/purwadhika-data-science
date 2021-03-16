def findPattern(numbers):
  diff1 = numbers[1] - numbers[0]
  diff2 = numbers[2] - numbers[1]

  div1 = numbers[1]/numbers[0]
  div2 = numbers[2]/numbers[1]

  if diff1 == diff2:
    print("AP " + str(numbers[2]+diff1))
  elif div1 == div2:
    print("GP " + str(numbers[2]*div1))


while True:
  numbers_str = (input("").split(' '))
  numbers = [int(i) for i in numbers_str]

  if numbers[0] == 0 and numbers[1] == 0 and numbers[2] == 0:
    break

  findPattern(numbers)