def arithmetic_series(number_of_terms, first_term, last_term):
    """
    The Arithmetic Series is the sum of an Arithmetic Progression
    
    Args:
        number_of_terms   Number of terms in the series
        first_term        The first term
        last_Term         The last term

    Returns:
        The value of the Arithmetic Series
    """
    return number_of_terms * (first_term + last_term) / 2

def is_multiple(value, divisor):
    """
    Determine if one number is a multiple of another

    Args:
        value             The value to check
        divisor           The number to divide into the value

    Returns:
        True if the numbers divide evenly, False otherwise
    """
    if divisor == 0: return False
    if value % divisor == 0: return True
    return False
    