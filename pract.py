import os

os.system("cls")


def get_numbers_between(num1, num2):
    start = min(num1, num2) + 1
    end = max(num1, num2)
    numbers = []
    for i in range(start, end):
        numbers.append(i)
    return numbers


print(get_numbers_between(6, 2))
