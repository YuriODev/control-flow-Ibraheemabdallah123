# Your solution to Exercise 1
alex = int(input("enter alex's age: "))
tatyana = int(input("enter tatyana's age: "))
output = ""

if alex > tatyana:
  output = "Alex is the eldest."
elif tatyana > alex:
  output = "Tatyana is the eldest."
else:
  output = "Alex and Tatyana are of the same age."

print(output)
