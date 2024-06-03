# Your solution to Exercise 7
num1 = float(input("number 1 "))
num2 = float(input("number 2 "))
operation = input("operation")
if operation == "+":
  print(num1 + num2)
elif operation == "-":
  print(num1 - num2)
elif operation == "*":
  print(num1 * num2)
elif operation == "/" and num2 != 0:
  print(num1 / num2)
elif operation == "mod" and num2 != 0:
  print(num1 % num2)
elif operation == "pow":
  print(num1 ** num2)
elif operation == "div" and num2 != 0:
  print(num1 // num2)
else:
  print("Division by 0!")
