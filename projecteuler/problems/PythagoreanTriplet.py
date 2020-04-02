import math

from projecteuler.mathlibrary import MathLibrary
from .IEulerSolution import IEulerSolution

class PythagoreanTriplet(IEulerSolution):
    """
    Solution to problem 8
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """

    def __init__(self, problem_number = None):
        IEulerSolution.__init__(self)

    def compute(self):

        for a in range(1, 334):
            done = False
            b = a + 1
            while not done:
                c = 1000 - (a + b)
                if MathLibrary.square(a) + MathLibrary.square(b) == MathLibrary.square(c): return a * b * c
                b += 1
                if b >= c: done = True
