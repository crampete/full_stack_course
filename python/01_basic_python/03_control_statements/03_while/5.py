arbitrary_string = "python"

iterator = len(arbitrary_string) - 1  # let's go from behind


new_reversed_string = ''
while iterator >= 0:
    new_reversed_string = new_reversed_string + arbitrary_string[iterator]
    iterator -= 1

print(new_reversed_string)
