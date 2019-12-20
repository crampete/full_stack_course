def hours_minutes_to_seconds(hours, minutes):
    '''
        Converts duration from hours and minutes into seconds

        Parameters:
            hours (int): The number of hours

            minutes (int): The number of minutes

        Returns:
            seconds (int): The hours and minutes converted to seconds.

        Example Usage:
            hours_minutes_to_seconds(2, 30) -> 9000

    '''

    hours_in_seconds = hours * 3600
    minutes_in_seconds = minutes * 60

    return hours_in_seconds + minutes_in_seconds
