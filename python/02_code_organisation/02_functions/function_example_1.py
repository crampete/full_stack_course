def list_write(file_path, data_list):
    '''
        Takes in the file path and the list to be written.
        
        Parameters:
            file_path (string): The file to be created.

            data_list (list): The data to be written.
            The code attempts to convert each item in the
            list to a string before writing to the file.

        Returns:
            None
    '''

    fp = open(file_path, 'w')

    for item in data_list:
        fp.write(str(item) + "\n")

    fp.close()