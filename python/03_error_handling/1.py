my_list = ['orange', 'apple', 'avacado']


try:
    print("I would like to eat an")
    print(my_list[5])
except:
    # catches all exceptions
    print("Something went wrong. So I'm printing the entire list instead.")
    print(my_list)