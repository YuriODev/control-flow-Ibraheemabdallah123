# Your solution to Exercise 2
age = int(input( "Enter your age: "))
output = ""
if age <= 1:
  output = "You are an infant."
  print(output)
elif age < 13:
  output = "You are a child."
  print(output)
elif age < 20:
  output = "You are a teenager."
  print(output)
elif age > 19:
  output = "You are an adult."
  print(output)
