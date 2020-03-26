import math

from projecteuler.mathlibrary import MathLibrary
from .IEulerSolution import IEulerSolution

class SmallestMultiple(IEulerSolution):
    """
    Solution to problem 5
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    def __init__(self, problem_number = None):
        IEulerSolution.__init__(self)

    def compute(self):
        result = 0
        max = 20
        notDone = True

        while notDone:

            result += max * (max - 1)
            trial = max -2

            while MathLibrary.is_multiple(result, trial):

                trial -= 1
                if trial == 1:
                    notDone = False
                    break

        return result