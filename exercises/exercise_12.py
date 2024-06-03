# Your solution to Exercise 12
num = int(input("Enter a four digit number: "))
thousand = num // 1000
hundred = (num % 1000) // 100
tens = (num % 100) // 10
ones = num % 10
thousand = "*" if thousand % 2 == 0 else str(thousand)
hundred = "*" if hundred  % 2 == 0 else str(hundred)
tens = "*" if tens  % 2 == 0 else str(tens)
ones = "*" if ones  % 2 == 0 else str(ones)
print(thousand, hundred, tens, ones)
