# Your solution to Exercise 1
alex = int(input("enter alex's age: "))
tatyana = int(input("enter tatyana's age: "))
output = ""

if alex > tatyana:
  output = "alex is eldest"
elif tatyana > alex:
  output = "tatyana is eldest"
else:
  output = "they are of the same age"

print(output)
