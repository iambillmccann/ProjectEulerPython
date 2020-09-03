from functools import reduce

import math

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

def get_divisors(number):
    """
    Compuute a list of divisors of the parameter (number)

    Args:
        number      The number to find the divisors of

    Returns:
        A list of the divisors of number
    """
    divisors = []
    limit = math.floor( math.sqrt(number) + 1 )

    for  divisor in range(1, limit):
        if is_multiple(number, divisor):
            divisors.append(divisor)
            quotient = number / divisor
            if (divisor != quotient) and (number != divisor): divisors.append(quotient)

    return divisors

def get_prime(max):
    """
    Compute a list of prime number up to a max number

    Args:
        max               The largest number to check

    Returns:
        A list of prime numbers
    """
    prime_numbers = [2, 3, 5, 7]

    for number in range(9, max + 1, 2):

        is_prime = True
        for divisor in prime_numbers:
            if math.sqrt(number) < divisor: break
            if is_multiple(number, divisor): is_prime = False
        if is_prime: prime_numbers.append(number)
    
    return prime_numbers

def get_factors(number, prime_numbers):
    """
    Calculate the list of prime factors for a number

    ToDo: rewrite this with a while loop to see if there is performance improvement

    Args:
        number            The number to find the factors of
        prime_numbers     The list of prime numbers

    Returns:
        A list of prime factors
    """
    factors = list()
    for prime_number in prime_numbers:
        if math.sqrt(number) < prime_number: break
        if is_multiple(number, prime_number):
            factors.append(prime_number)
            next_number = number / prime_number
            if next_number in prime_numbers: factors.append(next_number)
            else: factors = factors + get_factors(next_number, prime_numbers)
            break

    return factors

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

def reverse_digits(number):
    """
    Reverse the order of digits in an integer such that 1234 becomes 4321

    Args:
        number             The number to reverse

    Returns:
        The number with digits reversed
    """
    result = 0
    work_number = number

    while work_number > 0:
        remainder = work_number % 10
        result = result * 10 + remainder
        work_number = int(work_number / 10)

    return result

def series_product(numbers):
    return reduce( lambda x, y: x * y, numbers )

def series_sum(numbers):
    return reduce( lambda x, y: x + y, numbers )

def square(number):
    return number * number

def sum_natural(number):
    """
    Compute the sum of natural numbers up to and including number.
    """
    result = 0
    if number < 1: return result
    for sequence in range(1, number + 1): result += sequence
    return result

def sum_natural_squares(number):
    """
    Compute the sum of squares for natural numbers up to and including number.
    """
    result = 0
    if number < 1: return result
    for sequence in range(1, number + 1): result += square(sequence)
    return result