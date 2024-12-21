number = int(input("Enter the number: "))
power = int(input("Enter the power: "))
result = 1

for i in range(power):
  result *= number

  print("{} to the power of {} is {}".format(number, power, result))
