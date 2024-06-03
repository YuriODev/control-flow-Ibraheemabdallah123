# Your solution to Exercise 4
grade = int(input("enter your grade "))
if grade < 4:
  print("initial level")
elif grade < 7:
  print("average level")
elif grade < 10:
  print("sufficient level")
elif grade < 13:
  print("high level")
else:
  print("level is absent")
