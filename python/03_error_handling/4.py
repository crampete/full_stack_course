def write_data_to_file(file_path, data):
    try:
        fp = open(file_path, 'w')
    except:
        print("Error opening file.")
        return -1 # unsuccessful

    status = 0

    try:
        fp.write(data)
    except:
        status = -1
        print("An exception occurred while writing data.")
    else:
        print("Successfully wrote to file.")
    finally:
        fp.close()

    return status


# invalid file open. File doesn't even open
write_data_to_file('?', 'hi')

# Trying to write wrong data type to the file.
write_data_to_file('example.txt', 42)

# working example
write_data_to_file('example_2.txt', "Welcome to Crampete.")
    