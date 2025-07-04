import random
import string

def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_lowercase
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level. Using default (strong).")
        characters = string.ascii_letters + string.digits + string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

try:
    length = int(input("Enter the desired password length: "))
    print("Choose password complexity:")
    print("1 - Easy (lowercase letters only)")
    print("2 - Medium (letters and digits)")
    print("3 - Strong (letters, digits, symbols)")
    complexity = int(input("Enter your choice (1/2/3): "))

    if length <= 0:
        print("Password length must be a positive number.")
    else:
        password = generate_password(length, complexity)
        print("Generated Password:", password)

except ValueError:
    print("Please enter valid numbers.")
