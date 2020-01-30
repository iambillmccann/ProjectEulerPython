from .IEulerSolution import IEulerSolution

class Multiple3or5(IEulerSolution):
    """
    
    """
    def __init__(self, problem_number = None):
        IEulerSolution.__init__(self)

    def compute(self):
        return "3.1415926"