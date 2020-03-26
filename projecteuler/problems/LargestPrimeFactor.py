import math

from projecteuler.mathlibrary import MathLibrary
from .IEulerSolution import IEulerSolution

class LargestPrimeFactor(IEulerSolution):
    """
    Solution to problem 3, Find the largest prime factor of 600,851,475,143
    """
    VALUE = 600851475143

    def __init__(self, problem_number = None):
        IEulerSolution.__init__(self)

    def compute(self):
        factors = MathLibrary.get_factors(self.VALUE, MathLibrary.get_prime(10000))
        return int(factors[-1])
