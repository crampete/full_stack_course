# Raising errors
user_number = input("Please enter your number prefixed with +91.")

assert user_number[:3] == "+91", "You didn't enter +91 in the start"

print("We will send you a message very soon.")