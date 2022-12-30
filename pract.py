import os

os.system("cls")


def get_numbers_between(start, end):
    numbers = []
    if start < end:
        for i in range(start + 1, end):
            numbers.append(i)
    else:
        for i in range(end + 1, start):
            numbers.append(i)
    return numbers


for x in range(2 + 1, 7):
    print(x)
