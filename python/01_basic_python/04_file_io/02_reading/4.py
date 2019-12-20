# Reading character by characters

fp = open('4.character_by_character.txt', 'r')

while True:
    # you can read more than one character by specifying fp.read(2) and so on.
    character = fp.read(1)


    if not character:
        # end of file
        print("Reached end of file. So exiting.")
        break

    print(character)