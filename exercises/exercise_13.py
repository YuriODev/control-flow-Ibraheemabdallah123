# Your solution to Exercise 13
num = int(input("Enter a number"))
thousand = num // 1000
hundred = (num % 1000) // 100
tens = (num % 100) // 10
ones = num % 10
unique = (thousand != hundred or thousand == 0 or hundred == 0) and \
            (thousand != tens or thousand == 0 or tens == 0) and \
            (thousand != ones or thousand == 0) and \
            (hundred != tens or hundred == 0 or tens == 0) and \
            (hundred != ones or hundred == 0) and \
            (tens != ones or tens == 0)
print(unique)
