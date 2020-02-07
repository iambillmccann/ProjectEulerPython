from .IEulerSolution import IEulerSolution

class GenericSolution(IEulerSolution):
    """
    The default class when no solution has been provided for the problem.
    """
    def __init__(self, problem_number = None):
        IEulerSolution.__init__(self)

    def compute(self):
        return "The requested problem has not been solved."