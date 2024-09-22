#for loop multiplication table
number = int(input("Enter a number to see its multiplication table: ")

for x in range(1, 10):
  z = number * x
  print(f"{number} * {x} = {z}", end = "\t")
