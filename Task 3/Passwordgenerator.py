import random
import string

capitals = string.ascii_uppercase
letters = string.ascii_lowercase
digits = string.digits
special = string.punctuation

while True:
    try:
        user_input = int(input("How many characters do you want in your password? "))
        if user_input < 1:
            print("Password length must be at least 1.")
            continue
        break
    except ValueError:
        print("Please, enter numbers only.")

character_list = capitals + letters + digits + special

password = [random.choice(character_list) for _ in range(user_input)]

print("The random password is:", "".join(password))
