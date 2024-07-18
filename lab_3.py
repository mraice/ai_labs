print("<---------------Task 1--------------->")
nl = []

# Iterate through numbers from 1500 to 2700 (inclusive)
for x in range(1500, 2701):
    # Check if the number is divisible by 7 and 5 without any remainder
    if (x % 7 == 0) and (x % 5 == 0):
        # If the conditions are met, convert the number to a string and append it to the list
        nl.append(str(x))


print(',\t'.join(nl))


print("<---------------Task 2--------------->")
class tempconvert():
    def __init__(self):
        self.temp = 0
        self.temp_type = ""
        self.temp_types = ["c", "f"]

    def convert(self):
        if self.temp_type == "c":
            print(f"{self.temp}°C is {self.temp * 9/5 + 32}°F")
        elif self.temp_type == "f":
            print(f"{self.temp}°F is {(self.temp - 32) * 5/9}°C")
        else:
            print("Invalid input")

    def start(self):
        self.temp = int(input("Enter temperature: "))
        self.temp_type = input("Enter temperature type (C or F): ").lower()
        self.convert()

A = tempconvert()
A.start()


print("<---------------Task 3--------------->")

import random


def number_guessing_game():
    number_to_guess = random.randint(1, 9)
    while True:
        user_guess = input("Guess a number between 1 to 9: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
            if user_guess == number_to_guess:
                print("Well guessed!")
                break
            else:
                print("Try again.")
        else:
            print("Invalid input. Please enter a number.")


number_guessing_game()
print("<---------------Task 4--------------->")
i = 0
while i <= 5:
    print("* " * i)
    i += 1
i -= 2
while i != 0:
    print("* " * i)
    i -= 1

print("<---------------Task 5--------------->")
def reverse_string(string):
    return string[::-1]
str = input("Enter String to reverse: ")
str = reverse_string(str)
print(str)

print("<---------------Task 6--------------->")
def count_even_odd(numbers):
    count_odd = 0
    count_even = 0
    for num in numbers:
        if num % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd


series_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_count, odd_count = count_even_odd(series_of_numbers)

print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")


print("<---------------Task 7--------------->")
datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), 15, 121, {"class": 'IV'}, 8]

for item in datalist:
    print(f"Item: {item} - Type: {type(item)}")


print("<---------------Task 8--------------->")
for x in range(7):
    if x == 3 or x == 6:
        continue
    print(x)

print("<---------------Task 9--------------->")
def fibonacci_series(max_value):
    num1, num2 = 0, 1
    while num1 <= max_value:
        print(num1, end=" ")
        num1, num2 = num2, num1 + num2


fibonacci_series(50)

print("<---------------Task 10--------------->")
x: int = input("Enter Number of Rows: ")
y: int = input("Enter Number of Columns: ")

def create_2d_array(rows, columns):
    # use list comprehension to generate the 2d array
    return [[i * j for j in range(columns)] for i in range(rows)]


# test the function
print(create_2d_array(x, y))

print("<---------------Task 11--------------->")
str1 = ""
t = ""
while True:
    t = str(input("Enter String (Blank line to terminate): "))
    if (t == ""):
        break
    t += "\n"
    str1 += t
    t = ""
print(f"Here's your Lines: {str1.lower()}")

print("<---------------Task 12--------------->")
# Accepts a sequence of binary numbers and prints those divisible by 5
binary_numbers = input("Enter binary numbers separated by a comma: ").split(',')
divisible_by_five = [num for num in binary_numbers if int(num, 2) % 5 == 0]
print(",".join(divisible_by_five))

print("<---------------Task 13--------------->")
# Accepts a string and calculates the number of letters and digits
s = input("Enter a string: ")
letters = digits = 0
for char in s:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1
print(f"Letters {letters}\nDigits {digits}")

print("<---------------Task 14--------------->")
import re

def validate_password(password):
    if (len(password) >= 6 and
        re.search("[a-z]", password) and
        re.search("[A-Z]", password) and
        re.search("[0-9]", password) and
        re.search("[$#@]", password)):
        return True
    else:
        return False

# Example usage:
password_to_test = input("Enter the password to validate: ")
if validate_password(password_to_test):
    print("Password is valid.")
else:
    print("Password is invalid.")
