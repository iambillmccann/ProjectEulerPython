import math

from projecteuler.mathlibrary import MathLibrary
from .IEulerSolution import IEulerSolution

class SummationPrimes(IEulerSolution):
    """
    Solution to problem 10
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
    """

    def __init__(self, problem_number = None):
        IEulerSolution.__init__(self)

    def compute(self):
        primeNumbers = MathLibrary.get_prime(2000000)
        return MathLibrary.series_sum(primeNumbers)