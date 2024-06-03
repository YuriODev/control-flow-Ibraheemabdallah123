# Your solution to Exercise 10
point1 = int(input("input the x of a point on a graph"))
point11 = int(input("input the y of a point on a graph"))
point2 = int(input("input the x of a point on a graph"))
point22 = int(input("input the y of a point on a graph"))
point3 = int(input("input the x of a point on a graph"))
point33 = int(input("input the y of a point on a graph"))
side1 = (point2-point1)**2 + (point22-point11)**2
side2 = (point3-point2)**2 + (point33-point22)**2
side3 = (point1-point3)**2 + (point11-point33)**2
if side1 == 0 or side2 == 0 or side3 == 0:
  print("No")
elif side1 + side2 == side3 or side2 + side3 == side1 or side3 + side1 == side2:
  print("Yes")
else:
  print("No")
