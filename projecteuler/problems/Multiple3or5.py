import time
import math
from projecteuler.mathlibrary import MathLibrary
from .IEulerSolution import IEulerSolution

class Multiple3or5(IEulerSolution):
    """
    Solution to problem 1, Multiples of 3 or 5
    """
    range_start = 1
    range_stop  = 1000

    def __init__(self, problem_number = None):
        IEulerSolution.__init__(self)

    def compute_sum(self, first_term, difference):
        number_of_terms = math.floor((self.range_stop - self.range_start) / difference)
        last_term = first_term + difference * (number_of_terms - 1)
        return MathLibrary.arithmetic_series(number_of_terms, first_term, last_term)

    def compute(self):

        sum3 = self.compute_sum(3, 3)
        sum5 = self.compute_sum(5, 5)
        sum15 = self.compute_sum(15, 15)

        return int(sum3 + sum5 - sum15)