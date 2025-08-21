import random

char_list = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for char in range(0, nr_letters):
    add_char = random.choice(letters)
    char_list.append(add_char)

for char in range(0, nr_symbols):
    add_char = random.choice(symbols)
    char_list.append(add_char)

for char in range(0, nr_numbers):
    add_char =  random.choice(numbers)
    char_list.append(add_char)

random.shuffle(char_list)
total = nr_letters+nr_symbols+nr_numbers

for char in char_list:
    password += char

print(password)
