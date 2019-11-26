def invert_dictionary(source_dictionary):
    new_dictionary = {}

    for key, value in source_dictionary.items():
        new_dictionary[value] = key


    return new_dictionary