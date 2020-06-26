from importlib import import_module

def get_solution(problem_number, *args, **kwargs):
    """ Factory Pattern to select a class that runs the solution
    The ProblemFactory class using the factory pattern to return the solution to a
    given problem number.

    Args:
        problemNumber The number of the problem.

    Returns:
        The class that will solve the problem.
    """

    options = { 0 : "GenericSolution",
        1 : "Multiple3or5", 
        2 : "EvenFibonacci",
        3 : "LargestPrimeFactor",
        4 : "LargestPalindromeProduct",
        5 : "SmallestMultiple",
        6 : "SumSquareDifference",
        7 : "Prime10001",
        8 : "LargestProductSeries",
        9 : "PythagoreanTriplet",
        10 : "SummationPrimes",
        11 : "LargestProductGrid",
        12 : "HighlyDivisibleTriangle" }

    solution_class = options[problem_number]

    the_module = import_module(".{}".format(solution_class), "projecteuler.problems")
    the_class = getattr(the_module, solution_class)
    instance = the_class(*args, **kwargs)

    return instance
