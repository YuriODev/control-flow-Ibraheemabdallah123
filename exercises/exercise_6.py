# Your solution to Exercise 6
point1 = int(input("input the x of a point on a graph"))
point11 = int(input("input the y of a point on a graph"))
point2 = int(input("input the x of a point on a graph"))
point22 = int(input("input the y of a point on a graph"))
if point1 + point11 < point2 + point22:
  print("A is closer to the origin")
elif point1 + point11 > point2 + point22:
  print("B is closer to the origin")
else:
  print("A and B are the same distance from the origin")
