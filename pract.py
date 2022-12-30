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


print(get_numbers_between(1, 5))
print(get_numbers_between(5, 1))
