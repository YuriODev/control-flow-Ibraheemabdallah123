# Your solution to Exercise 9
num = input("enter a 3 digit number")
if int(num[0]) + int(num[2]) > int(num[1]):
  print(">")
elif int(num[0]) + int(num[2]) < int(num[1]):
  print("<")
else:
  print("=")
