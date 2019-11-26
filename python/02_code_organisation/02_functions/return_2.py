def capture_information():
    name = input("Your name please.\n")
    return name
    print("This does not get executed")


user_name = capture_information()
print("Username is " + user_name)

