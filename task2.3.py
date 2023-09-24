num = int(input("Введите количество ступенек пирамиды: "))


def f_str(i):
    s = ""
    if i < 10:
        s = "  "
    elif i < 100:
        s = " "
    return s + str(i)


pyramid = ""
for j in range(1, num + 2):
    row = " " * 4 * (num + 2 - j)
    for i in range(1, j):
        s = f_str(i)
        row += s + " "
    for i in range(j - 1, 1, -1):
        s = f_str(i - 1)
        row += s + " "

    row += "\n"
    pyramid += row

print(pyramid)