# Your solution to Exercise 2
age = int(input( "Enter your age: "))
output = ""
if age <= 1:
  output = "You are an infant"
  print(output)
elif age < 13:
  output = "you are a child"
  print(output)
elif age < 20:
  output = "you are a teenager"
  print(output)
elif age > 19:
  output = "you are an adult"
  print(output)
