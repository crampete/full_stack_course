def reverse_string(target_string):
    '''
        Takes in a string and reverses it.


        Parameters:
            target_string (string): The string to be reversed.


        Returns:
            The reversed string

    '''

    result_string = ''

    iterator = len(target_string) - 1 

    while iterator >= 0:
        result_string = result_string + target_string[iterator]
        iterator -= 1

    
    return result_string


