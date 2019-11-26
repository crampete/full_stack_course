# better way is to return True or False instead of a string
# Please check the next example for that
def even_or_odd(number_to_check):
    if number_to_check % 2 == 0:
        print("Even Number")
        return "Even"
    else:
        print("Odd Number")
        return "Odd"

    print("This does not get executed")


result = even_or_odd(1)
print(f"1 is an {result} number.")

print("2 is an " + even_or_odd(2) + " Number.")

