from abc import ABCMeta, abstractmethod

class IEulerSolution(metaclass = ABCMeta):
    """
    This is an abstract class for the Euler solutions
    """
    def __init__(self):
        object.__init__(self)

    @abstractmethod
    def compute(self):
        pass