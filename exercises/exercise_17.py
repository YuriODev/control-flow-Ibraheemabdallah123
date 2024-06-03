# Your solution to Exercise 17
ticket = input("whats the ticket number")
if int(ticket[0]) + int(ticket[1]) + int(ticket[2]) == int(ticket[3]) + int(ticket[4]) + int(ticket[5]):
  print("lucky")
else:
  print("ordinary")
