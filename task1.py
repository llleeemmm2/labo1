a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

count = 0

if a == b: count = 2
if a == c: count = 2
if b == c: count = 2

if a == b == c: count = 3
if a != b != c: count = 0
print(f"Number of matching numbers: {count}")