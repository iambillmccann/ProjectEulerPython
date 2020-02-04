import time
from .IEulerSolution import IEulerSolution

class Multiple3or5(IEulerSolution):
    """
    Solution to problem 1, Multiples of 3 or 5
    """
    def __init__(self, problem_number = None):
        IEulerSolution.__init__(self)

    def compute(self):
        time.sleep(2.33333)
        return "3.1415926"