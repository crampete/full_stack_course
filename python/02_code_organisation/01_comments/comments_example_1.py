#code used to remove vowels from a given string
my_string = "I am going to study for 2 hours everyday"
result_string = ''


vowels = ['a', 'e', 'i', 'o', 'u']

for character in my_string:
    # lowering character to remove capital vowels as well
    if character.lower() not in vowels:
        result_string += character


print(result_string)