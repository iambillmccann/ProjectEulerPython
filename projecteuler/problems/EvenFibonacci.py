import math

from projecteuler.mathlibrary import MathLibrary
from .IEulerSolution import IEulerSolution

class EvenFibonacci(IEulerSolution):
    """
    Solution to problem 2, Sum of even terms of a finbonacci sequence
    """
    LIMIT = 4000000

    def __init__(self, problem_number = None):
        IEulerSolution.__init__(self)

    def compute(self):

        result = 2
        term1 = 1
        term2 = 2

        sum = term1 + term2
        while (sum < self.LIMIT):

            if (MathLibrary.is_multiple(sum, 2)): result += sum
            term1 = term2
            term2 = sum
            sum = term1 + term2

        return int(result)
