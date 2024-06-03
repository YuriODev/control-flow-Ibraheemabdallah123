# Your solution to Exercise 16
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (month == 2 or month == 4 or month == 6 or month == 9 or month == 11) and (day == 1):
  print(f"31.{month - 1}.{year}")
elif (month == 2 or month == 4 or month == 6 or month == 9 or month == 11) and (day != 1):
  print(f"{day - 1}.{month}.{year}")
elif (month == 5 or month == 7 or month == 10 or month == 12) and (day == 1):
  print(f"30.{month - 1}.{year}")
elif (month == 5 or month == 7 or month == 10 or month == 12) and (day != 1):
  print(f"{day - 1}.{month}.{year}")
elif (month == 8) and (day == 1):
  print(f"31.{month - 1}.{year}")
elif (month == 8) and (day != 1):
  print(f"{day - 1}.{month}.{year}")
elif (month == 3) and (day == 1) and (year % 4 != 0):
  print(f"28.{month - 1}.{year}")
elif (month == 3) and (day != 1) and (year % 4 != 0):
  print(f"{day - 1}.{month}.{year}")
elif (month == 3) and (day == 1) and (year % 4 == 0):
  print(f"29.{month - 1}.{year}")
elif (month == 3) and (day != 1) and (year % 4 == 0):
  print(f"{day - 1}.{month}.{year}")
elif (month == 1) and (day == 1):
  print(f"31.12.{year - 1}")
elif (month == 1) and (day != 1):
  print(f"{day - 1}.{month}.{year}")
