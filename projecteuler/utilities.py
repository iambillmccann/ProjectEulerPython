import math

def format_milliseconds(total_time):
    """
    Format a python time value into HH:MM:SS:mmm
    Python time values are total second in a float. The decimal
    portion of the float is the fraction of a second.

    Args:
       total_time   The amount of time to format

    Returns:
        A string formatted as HH:MM:SS:mmm
    """

    milliseconds = math.floor(total_time % 1 * 1000)
    total_seconds = math.floor(total_time)
    total_minutes = math.floor(total_seconds / 60)
    seconds = int(math.floor(total_seconds % 60))
    minutes = int(math.floor(total_minutes % 60))
    hours = int(math.floor(total_minutes / 60))

    format_milliseconds = str(milliseconds)
    format_seconds = str(seconds)
    format_minutes = str(minutes)
    format_hours = str(hours)

    if milliseconds < 1: format_milliseconds = '000'
    elif milliseconds < 10: format_milliseconds = '00' + format_milliseconds
    elif milliseconds < 100: format_milliseconds = '0' + format_milliseconds

    if seconds < 10: format_seconds = '0' + format_seconds
    if minutes < 10: format_minutes = '0' + format_minutes
    if hours < 10: format_hours = '0' + format_hours

    return '{}:{}:{}.{}'.format(format_hours, format_minutes, format_seconds, format_milliseconds)
