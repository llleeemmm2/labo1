n = int(input("Enter natural number: "))
for i in range(1, n+1):
    print(' ' * (n + 1 - i), end='')
    for j in range(1, i+1):
        print(j, end='')
    for revs in range(i-1, 0, -1):
        print(revs, end='')
    print("")