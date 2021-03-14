import re

def sum_of_numbers(num1, num2):

    sum_contain = r"(3)"
    if num1 == 3 or num2 == 3:
        if re.search(sum_contain, total):
            return True
        else:
            return False

    else:
        return False
num1 = int(input("Enter a first number: "))
num2 = int(input("Enter another number: "))
total = str(num1 + num2)

print(sum_of_numbers(num1, num2))