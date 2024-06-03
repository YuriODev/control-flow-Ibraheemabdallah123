# Your solution to Exercise 15
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (month == 4 or month == 6 or month == 9 or month == 11) and (day >= 30):
  print(f"1.{month + 1}.{year}")
elif (month == 4 or month == 6 or month == 9 or month == 11) and (day < 30):
  print(f"{day + 1}.{month}.{year}")
elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10) and (day >= 31):
  print(f"1.{month + 1}.{year}")
elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and (day < 31):
  print(f"{day + 1}.{month}.{year}")
elif (month == 12) and (day == 31):
  print(f"1.1.{year + 1}")
elif (month == 2) and (day < 29) and (year % 4 == 0):
  print(f"{day + 1}.{month}.{year}")
elif (month == 2) and (day >= 29) and (year % 4 == 0):
  print(f"1.{month + 1}.{year}")
elif (month == 2) and (day < 28) and (year % 4 != 0):
  print(f"{day + 1}.{month}.{year}")
elif (month == 2) and (day >= 28) and (year % 4 != 0):
  print(f"1.{month + 1}.{year}")
