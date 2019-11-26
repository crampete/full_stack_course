# if no name is passed the student_name
# argument gets the value "Dear Friend"


def happy_birthday(student_name="Dear Friend"):
    print("Happy B'day " + student_name)
    print("Hope you have a great day")


# always put default parameters towards the end
def store_details(name, origin_country="China"):
    # China has the highest population in the world.
    # It's highly likely that a person is Chinese.
    print(f"{name} is from {origin_country}.")


def store_details(name, origin_country="China", age=20):
    print(f"{name} is from {origin_country}.")
    print(f"He/She is {age} years old.")

# so if no course list is passed it
# assumed an empty list
def courses_taken(course_list=[]):
    if len(course_list) == 0:
        print("No courses taken.")
    else:
        print(course_list)


happy_birthday("Karthik")

store_details("Abhirath", "India")
store_details("Bruce Lee")

courses_taken(["Math 2", "Science", "Social"])
courses_taken()

# some invalid calls
# store_details() # name is mandatory.

# SyntaxError: positional argument follows keyword argument
# order is wrong and it confuses Python.
# store_details(origin_country="India", "Abhirath")
