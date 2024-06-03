# Your solution to Exercise 3
num = int(input("Enter a number 1 - 36: "))
if num > 0 and num < 11:
  if num % 2 == 0:
    print("Black")
  else:
    print("Red")
elif num > 10 and num < 19:
  if num % 2 == 0:
    print("Red")
  else:
    print("Black")
elif num > 18 and num < 29:
  if num % 2 == 0:
    print("Black")
  else:
    print("Red")
elif num > 28 and num < 37:
  if num % 2 == 0:
    print("Red")
  else:
    print("Black")
elif num > 36:
  print("The bet will not play!")
else:
  print("Green")
