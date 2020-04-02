import math

from projecteuler.mathlibrary import MathLibrary
from .IEulerSolution import IEulerSolution

class Prime10001(IEulerSolution):
    """
    Solution to problem 7
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
    """

    def __init__(self, problem_number = None):
        IEulerSolution.__init__(self)

    def compute(self):

        max_prime = 8000
        prime_numbers = MathLibrary.get_prime(max_prime)
        return prime_numbers[1000]  # The 1001th element of the list is [1000]
