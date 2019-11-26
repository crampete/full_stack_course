
def is_even(number_to_check):
    if number_to_check % 2 == 0:
        return True
    else:
        return False


user_entered_number = int(input("Please enter an even number."))

if is_even(user_entered_number) == True:
  print("Thank you for the even number.")
else:
  print("Odd numbers are not allowed.")