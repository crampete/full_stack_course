# Raising errors
user_input = input("Please enter y or n.")

# this can also be wrapped in a try except and be handled
if user_input == 'y':
    print("You've entered YES.")
elif user_input == 'n':
    print("You've entered NO.")
else:
    # we can raise our own errors using raise.
    # these raised errors can be caught using try and except statements.
    raise Exception("You've entered something else. Raising an error.")