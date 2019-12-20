my_list = ['apple', 'orange', 'avacado']
try:
    print("I would like to eat an")
    print(b)
    print(my_list[5])

except IndexError:
    # catches index errors
    print("You have entered an invalid index.")
except NameError:
    # catches name errors. Invalid variable names
    print("You have used a variable that doesn't exist :)")
except:
    print("Something went wrong.")